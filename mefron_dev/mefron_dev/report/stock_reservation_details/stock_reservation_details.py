import frappe

@frappe.whitelist()
def execute(filters=None):
    columns = [
        {
            "label": ("ID"),
            "fieldname": "id",
            "width": 165,
            "hidden": 1
        },
        {
            "label": ("Sales Order ID"),
            "fieldname": "sales_order_id",
            "fieldtype": "Link",
            "options": "Sales Order",
            "width": 165,
        },
        {
            "label": ("Item"),
            "fieldname": "item_code",
            "fieldtype": "Link",
            "options": "Item",
            "width": 100,
        },
        {
            "label": ("Customer"),
            "fieldname": "customer",
            "width": 165,
        },
        {
            "label": ("Sales Order Date"),
            "fieldname": "so_date",
            "width": 160,
        },
        {
            "label": ("Ordered Qty"),
            "fieldname": "qty",
            "width": 100,
        },
        {
            "label": ("Dispatch Qty"),
            "fieldname": "to_delivered_qty",
            "width": 100,
        },
        {
            "label": ("To Reserve Qty"),
            "fieldname": "to_reserv_qty",
            "width": 100,
        },
        {
            "label": ("Stock Reserved Qty"),
            "fieldname": "reserved_qty",
            "width": 100,
        },
        {
            "label": ("Reserve"),
            "fieldname": "reserve",
            "fieldtype": "Button",
            "width": 100,
            "click": "custom_function_name"  # Define the custom function to be called on button click
        },
        {
            "label": ("Unreserve"),
            "fieldname": "unreserve",
            "fieldtype": "Button",
            "width": 100,
            "click": "custom_function_name"  # Define the custom function to be called on button click
        }
    ]
    query = """
    SELECT 
        soi.name AS id,
        so.name AS sales_order_id,
        so.customer_name AS customer,
        so.transaction_date AS so_date,
        soi.item_code AS item_code,
        soi.qty AS qty,
        soi.delivered_qty AS to_delivered_qty,
        soi.stock_reserved_qty AS reserved_qty,
        SUM(sre.reserved_qty) - SUM(sre.delivered_qty) AS r_qty,
        (SUM(sre.reserved_qty - sre.delivered_qty)) + soi.delivered_qty AS a_dt,
        soi.qty - ((SUM(sre.reserved_qty - sre.delivered_qty)) + soi.delivered_qty) AS to_reserv_qty,
        CONCAT(
            '<button class="btn btn-primary pt-0 pb-0 reserv_qty" style="background-color: #458f27" ',
            'data-id="', soi.name, '" ',
            'data-sales-order-id="', so.name, '" ',
            'data-customer="', so.customer_name, '" ',
            'data-so-date="', so.transaction_date, '" ',
            'data-item-code="', soi.item_code, '" ',
            'data-qty="', soi.qty, '" ',
            'data-to-delivered-qty="', soi.delivered_qty, '" ',
            'data-reserved-qty="', soi.stock_reserved_qty, '" ',
            'data-to-reserve-qty="', (COALESCE(soi.stock_qty, 0) - 
            (COALESCE(soi.stock_reserved_qty, soi.delivered_qty * soi.conversion_factor))) / 
            COALESCE(soi.conversion_factor, 1), '" ',
            'data-warehouse="', soi.warehouse, '" ',
            '>Reserve</button>'
        ) AS reserve,
        CONCAT(
            '<button class="btn btn-primary pt-0 pb-0 unreserv_qty" style="background-color: #d35524" ',
            'data-id="', soi.name, '" ',
            'data-sales-order-id="', so.name, '" ',
            'data-customer="', so.customer_name, '" ',
            'data-so-date="', so.transaction_date, '" ',
            'data-item-code="', soi.item_code, '" ',
            'data-qty="', soi.qty, '" ',
            'data-to-delivered-qty="', soi.delivered_qty, '" ',
            'data-reserved-qty="', soi.stock_reserved_qty, '" ',
            'data-to-reserve-qty="', (COALESCE(soi.stock_qty, 0) - 
            (COALESCE(soi.stock_reserved_qty, soi.delivered_qty * soi.conversion_factor))) / 
            COALESCE(soi.conversion_factor, 1), '" ',
            'data-warehouse="', soi.warehouse, '" ',
            '>Unreserve</button>'
        ) AS unreserve
    FROM 
        `tabSales Order` so 
    LEFT JOIN `tabSales Order Item` AS soi 
        ON soi.parent = so.name 
    JOIN `tabStock Reservation Entry` AS sre 
        ON soi.name = sre.voucher_detail_no
    WHERE 
        so.status != 'Completed' 
        AND so.status != 'Cancelled' 
        AND soi.reserve_stock = 1
        AND sre.status != 'Delivered' 
        AND sre.status != 'Cancelled'
"""

    query_params = []

    if filters:
        if filters.get("item_code"):
            query += " AND soi.item_code = %s"
            query_params.append(filters.get("item_code"))
        if filters.get("set_warehouse"):
            query += " AND soi.warehouse = %s"
            query_params.append(filters.get("set_warehouse"))

    query += " GROUP BY soi.name ORDER BY soi.name DESC"

    data = frappe.db.sql(query, tuple(query_params), as_dict=True)

    return columns, data

