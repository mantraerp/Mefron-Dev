frappe.ui.form.on('Payment Entry', {
	onload:function(frm) {
		setTimeout(() => {
            frm.set_query('party_bank_account', () => {
                return {
                    filters: {
                        is_company_account: 0,
    					party_type: frm.doc.party_type,
    					party: frm.doc.party,
    					workflow_state: "Approved",
                    }
                };
            });
        }, 1000); // 1000 milliseconds = 1 second    
	}
});