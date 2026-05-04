// Copyright (c) 2026, Adil and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Member", {
//  refresh(frm) {

//  },
// });

frappe.ui.form.on('Inventory', {
	loan_id(frm,cd,cn) {
        let loan_id = frappe.model.get_value(cd,cn,"loan_id")
        frappe.db.get_value("Loan", 'ISSUE-0009', ["book_id", "book_title"])
            .then((r)=>{
                frappe.model.set_value(cd,cn,"book_id",r.message.book_id)
                frappe.model.set_value(cd,cn,"book_title",r.message.book_title)     
            });
	}
})