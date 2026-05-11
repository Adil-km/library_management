# Copyright (c) 2026, Adil and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import add_to_date
from frappe.website.website_generator import WebsiteGenerator


class Loan(WebsiteGenerator):
	def validate_book_availbale(self):
		curr_book = f"{self.book_title} - {self.book_id}"
		if frappe.get_doc("Book Item", self.book_id).status != "Available":
			frappe.throw(f"{curr_book} is already Issued or not Available.")

	def before_save(self):		
		self.validate_book_availbale()

	def on_submit(self):
		self.validate_book_availbale()
		frappe.db.set_value("Book Item", self.book_id, "status", "Issued")
	
	def on_cancel(self):
		frappe.db.set_value("Book Item", self.book_id, "status", "Available")