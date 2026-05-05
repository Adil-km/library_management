// Copyright (c) 2026, Adil and contributors
// For license information, please see license.txt

frappe.ui.form.on("Member", {
    onload: function(frm) {
        frm.set_query("loan_id", "books", function() {
            return {
                filters: [
                    ["member_id", "=" ,frm.doc.name]
                ]
            };
        })
    },

});