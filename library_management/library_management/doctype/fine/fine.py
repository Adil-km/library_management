# Copyright (c) 2026, Adil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Fine(Document):
	def before_save(self):
		book_id = frappe.get_doc("Book Item",self.book_item).book
		self.book_title = frappe.get_doc("Book", book_id).title
		
		if self.rate_per_day < 1:
			frappe.throw("Rate Per Day field must be greater than 1.")
		if self.days_overdue < 1:
			frappe.throw("Days Overdue field must be greater than 1.")
	
		self.total_amount = self.days_overdue * self.rate_per_day 