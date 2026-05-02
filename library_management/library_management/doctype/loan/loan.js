// Copyright (c) 2026, Adil and contributors
// For license information, please see license.txt

frappe.ui.form.on("Loan", {
	issue_date : function(frm) {
        let issue_date = frm.doc.issue_date
        let days = 14
        let due_date = frappe.datetime.add_days(issue_date, days)
        frm.set_value("due_date", due_date)
    },
    book_id : function(frm){
        if (frm.doc.book_id) {
            frappe.db.get_value('Book Item', frm.doc.book_id, 'book')
                .then(r => {
                    let book_name = r.message.book;
                    return  frappe.db.get_value('Book', book_name, 'title')
                })
                .then(r =>{
                    frm.set_value("book_title",r.message.title)
                });
        }
    },
    member_id : function(frm){
        if (frm.doc.member_id) {
            frappe.db.get_value('Member', frm.doc.member_id, 'full_name')
                .then(r =>{
                    frm.set_value("member_name",r.message.full_name)
                });
        }
    }
});
