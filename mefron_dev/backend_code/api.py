import frappe
import random
from frappe.utils import now
from frappe.email.queue import flush
from datetime import datetime, timedelta
from frappe.core.doctype.activity_log.activity_log import add_authentication_log
from frappe.auth import LoginManager
import string

@frappe.whitelist()
def get_party_name(party_type,party):
    if party_type == "Supplier":
        sup_name = frappe.db.sql("select supplier_name from `tabSupplier` where name = %s ", (party), as_dict = True)
        if sup_name :
            supplier_name = sup_name[0]["supplier_name"]
            return supplier_name
    elif party_type == "Customer":
        cust_name = frappe.db.sql("select customer_name from `tabCustomer` where name = %s ", (party), as_dict = True)
        if cust_name :
            customer_name = cust_name[0]["customer_name"]
            return customer_name
    elif party_type == "Employee":
        emp_name = frappe.db.sql("select employee_name from `tabEmployee` where name = %s ", (party), as_dict = True)
        if emp_name :
            employee_name = emp_name[0]["employee_name"]
            return employee_name
    else:
        frappe.msgprint("Not Found")
        
@frappe.whitelist()
def warehouse_manager_data_fetch_stock_entry(mr_no):
    tw = frappe.db.sql("SELECT set_warehouse FROM `tabMaterial Request` WHERE name = %s", (mr_no,))

    set_tw = tw[0][0]  # Extracting the value from the first tuple in the list
    # frappe.msgprint(set_tw)

    warehouse_manager = []

    wm = frappe.db.sql("select warehouse_manager from `tabWarehouse Manager` where parent = %s ", (set_tw,))

    # for record in wm:
    #     warehouse_manager.append(record["warehouse_manager"])

    # Assign the string to frappe.response["message"]
    return wm    

@frappe.whitelist()
def warehouse_manager_data_fetch_material_request(warehouse):
    warehouse_manager = []

    wm = frappe.db.sql("select warehouse_manager from `tabWarehouse Manager` where parent = %s ",(warehouse))
                
    # for record in wm:
    #         warehouse_manager.append(record)

    return wm
# Check User & then end Otp On Email
@frappe.whitelist(allow_guest=True)
def send_otp(email):
    filters = {
        "email": email,
        "enabled":1
    }
    #check user are exists or not
    userexists = frappe.db.exists("User", filters)
    
    # If record exists, return True
    if userexists:
        otpsend = frappe.db.exists("Email OTP", {"email_id":email})
        numeric_characters = string.digits
        alphabet_characters = string.ascii_letters
    
        # Generate the OTP with 2 numeric characters and 1 alphabetical character
        otp1 = ''.join(random.choices(numeric_characters, k=2)) + random.choice(alphabet_characters)
        otp2 = random.choice(numeric_characters) + ''.join(random.choices(alphabet_characters, k=2))

        
        email_otp=otp1+otp2
        if otpsend:
            # Update Send otp Log
            new_otp=frappe.get_doc("Email OTP",email)
            new_otp.email_otp=email_otp
            new_otp.datetime=now()
            new_otp.save()
            frappe.db.commit()
            full_name=new_otp.full_name
            send_email(email,email_otp,full_name)
        else:
            # Create Send otp Log
            # frappe.msgprint("new login")
            new_otp=frappe.new_doc("Email OTP")
            new_otp.email_id=email
            new_otp.email_otp=email_otp
            new_otp.datetime=now()
            new_otp.insert(ignore_permissions=True)
            frappe.db.commit()
            full_name=new_otp.full_name
            send_email(email,email_otp,full_name)

        return "Done"
    else:
        frappe.msgprint("User with email {} does not exist".format(email))
        return "Error"
 # this function for a email formate  
def send_email(email,email_otp,full_name):
    frappe.sendmail(
        recipients=email,
        subject="OTP Verification",
        message=f"""
        <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<div style="padding: 1%;background-color: #f4f5f6">
    <div class="box" style="  background-color: #fff;
        padding: 25px;
        border-radius:15px;        
        width: 60%;
        align-items: center;
        margin-top: 100px;
        margin-bottom: 100px;
        margin-left: auto;
        margin-right: auto;">
        <h2>Dear {full_name},</h2>
        <p>Please use the verification code below to sign in.</p>
        <p>Login Attempted at {now()}</p>
        <h1>{email_otp}</h1>
        <h4>OTP will expire in 10 minutes.</h4>
        <p>Thank You</p>
        <img src="https://mefron.milaap.ai/files/Mefron_Logo_CC_V14.png">
    </div>
    </div>
</body>
</html>""" 
    )
    send = flush()
    
@frappe.whitelist(allow_guest=True)
#yhis function for verify a otp
def verify_otp(email,otp):
    r_send = frappe.get_doc("Email OTP",email)	
    check_otp = r_send.email_otp
    check_time = r_send.datetime
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    #change Date formate
    ck_time = datetime.strptime(str(check_time) , date_format)
    end_date = now()

    dt_object = datetime.strptime(end_date , date_format)
    start_date = dt_object - timedelta(hours=0, minutes=10)
    #check Otp
    if start_date < ck_time:
        print("if")
        if check_otp==otp:
            #enquiry(mobile,equipment_id)
            user=email
            login_user(user)
            return "Done"
        else:
            return "Error"
    else:
        return "Expired"
	

@frappe.whitelist(allow_guest=True)
# this function for ligin
def login_user(user):
    # frappe.msgprint("Test login_user")
    number = frappe.db.get_value("User", user, ['phone'])
    frappe.local.login_manager.user = user
    frappe.local.login_manager.post_login()
    frappe.db.commit()
    
    user_name = frappe.db.sql("select first_name from `tabUser` where name=%s ",user)
    
    user = frappe.session.user
    subject = user_name[0][0]+" logged in"

    if number:
        add_authentication_log(subject,user)
        
    
    

    login_token = frappe.generate_hash(length=32)
    frappe.cache().set_value(
        f"login_token:{login_token}", frappe.local.session.sid, expires_in_sec=120
    )
    
   
    # print("\n\n login token", login_token, "\n\n")
    # return login_token
    return login_via_token(login_token, number,user)

#login with otp
@frappe.whitelist(allow_guest=True)
def login_via_token(login_token: str, number,user):
    sid = frappe.cache().get_value(f"login_token:{login_token}", expires=True)
    if not sid:
        frappe.respond_as_web_page(_("Invalid Request"), _(
            "Invalid Login Token"), http_status_code=417)
        return

    frappe.local.form_dict.sid = sid
   
    frappe.local.login_manager = LoginManager()
    
    return True