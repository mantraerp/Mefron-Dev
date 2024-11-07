app_name = "mefron_dev"
app_title = "Mefron Dev"
app_publisher = "Foram Shah"
app_description = "Mefron Dev"
app_email = "foram@sanskartechnolab.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mefron_dev/css/mefron_dev.css"
app_include_js = "/assets/mefron_dev/js/email_button.js"


# include js, css files in header of web template
# web_include_css = "/assets/mefron_dev/css/mefron_dev.css"
# web_include_js = "/assets/mefron_dev/js/mefron_dev.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mefron_dev/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Material Request": "public/js/material_request_changes.js",
    "Stock Entry": "public/js/stock_entry.js",
    "Payment Entry": "public/js/payment_entry.js",
    "Purchase Invoice": "public/js/purchase_invoce.js",
    "Subcontracting Receipt": "public/js/subcontracting_receipt.js",
    "Subcontracting Order": "public/js/subcontracting_order.js",
    "Journal Entry": "public/js/journal_entry.js",
    "Purchase Receipt": "public/js/purchase_receipt.js",
    "Sales Invoice": "public/js/sales_invoice.js",
    "Tax Category": "public/js/tax_category.js",
    "Payment Request": "public/js/payment_request.js",
    "Sales Order": "public/js/sales_order.js",
    "Purchase Order": "public/js/purchase_order.js",
    "Delivery Note": "public/js/delivery_note.js",
}
# doctype_js=  {"Sales Invoice" : "public/js/sales_invoice.js"}

# doctype_list_js = {"Material Request" : "public/js/material_request.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "mefron_dev/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "mefron_dev.utils.jinja_methods",
# 	"filters": "mefron_dev.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mefron_dev.install.before_install"
# after_install = "mefron_dev.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mefron_dev.uninstall.before_uninstall"
# after_uninstall = "mefron_dev.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "mefron_dev.utils.before_app_install"
# after_app_install = "mefron_dev.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "mefron_dev.utils.before_app_uninstall"
# after_app_uninstall = "mefron_dev.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mefron_dev.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Override standard doctype classes

# override_doctype_class = {
# 	"Sales Order": "mefron_dev.backend_code.sales_orders.sales_orders.SalesOrder"
# }



override_doctype_class = {
	"Purchase Invoice": "mefron_dev.purchase_invoice.PurchaseInvoice",
    "Purchase Receipt": "mefron_dev.purchase_receipt.PurchaseReceipt",
    "Material Request": "mefron_dev.material_request.MaterialRequest",
    "Subcontracting Order": "mefron_dev.backend_code.subcontracting.subcontracting_order.SubcontractingOrder",
    "Stock Reservation Entry": "mefron_dev.backend_code.stock_reservation_entry.stock_reservation_entry.StockReservationEntry"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Sales Invoice": {
        "on_submit": "mefron_dev.backend_code.sales_invoice.sales_invoice.make_dc"
    },
    "Subcontracting Receipt": {
        "before_submit": "mefron_dev.backend_code.subcontracting.subcontracting_receipt.make_stock_entry"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mefron_dev.tasks.all"
# 	],
# 	"daily": [
# 		"mefron_dev.tasks.daily"
# 	],
# 	"hourly": [
# 		"mefron_dev.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mefron_dev.tasks.weekly"
# 	],
# 	"monthly": [
# 		"mefron_dev.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "mefron_dev.install.before_tests"

# Overriding Methods
# ------------------------------
#
# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	"erpnext.selling.doctype.sales_order.sales_order.create_stock_reservation_entries":"mefron_dev.backend_code.sales_orders.sales_orders.create_stock_reservation_entries"
}

#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mefron_dev.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["mefron_dev.utils.before_request"]
# after_request = ["mefron_dev.utils.after_request"]

# Job Events
# ----------
# before_job = ["mefron_dev.utils.before_job"]
# after_job = ["mefron_dev.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"mefron_dev.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    "Workflow",
    "Workflow State",
    "Workflow Action Master",
    "Letter Head",
    {"dt": "Report", "filters": [["module", "in", ["Mefron Dev"]]]},
    {"dt": "Print Format", "filters": [["module", "in", ["Mefron Dev"]]]},
    {"dt": "Server Script"},
    {"dt": "Client Script"},
    {"dt": "Property Setter", "filters": [["module", "in", ["Mefron Dev"]]]},
    {"dt": "Custom DocPerm",},
    {"dt": "Document Naming Rule"},
    {"dt": "Role"},
]
