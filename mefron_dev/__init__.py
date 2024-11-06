__version__ = "0.0.1"

import erpnext.selling.doctype.sales_order.sales_order
import mefron_dev.backend_code.sales_order.sales_order


erpnext.selling.doctype.sales_order.sales_order.make_raw_material_request = mefron_dev.backend_code.sales_order.sales_order.make_raw_material_request

# /home/mantra/mefron-bench/apps/mefron_dev/mefron_dev/backend_code/sales_order/sales_order.py