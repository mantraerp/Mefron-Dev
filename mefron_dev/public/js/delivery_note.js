frappe.ui.form.on('Delivery Note', {
    onload(frm) {
        frm.set_query('set_warehouse', () => {
            return {
                filters: {
                    custom_is_sales_warehouse: 1
                }
            };
        });
        setTimeout(() => {
            frm.set_query('customer', () => {
                return {
                    filters: {
                        workflow_state: "Approved",
                    }
                };
            });
        }, 1000); // 1000 milliseconds = 1 second   
        frm.set_query('set_target_warehouse', () => {
            return {
                filters: {
                    custom_is_sales_warehouse: 1
                }
            };
        });
    }

});