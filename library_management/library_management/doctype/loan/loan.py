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

		if not self.member_name:
			self.member_name = frappe.get_value('Member', self.member_id, "full_name")
		
		if not self.book_title:
			item_id = frappe.db.get_value('Book Item', self.book_id, 'book')
			self.book_title = frappe.db.get_value('Book', item_id, 'title')

		if not self.due_date:
			days = 14
			self.due_date = add_to_date(self.issue_date, days=days)
	
	def before_validate(self):
		if self.name and not self.loan_id:
			self.loan_id = self.name

	def on_submit(self):
		self.validate_book_availbale()

		res_doc = frappe.get_doc("Reservation", self.reservation_id)
		if res_doc.status != "Active":
			frappe.throw(f"Member is not Active. Cannot add Loan for member {self.member_name}")

		# add child item in Reservation doctype
		child_row = res_doc.append('books', {
			'loan_id': self.loan_id,
		})
		res_doc.save()

		frappe.db.set_value("Book Item", self.book_id, "status", "Issued")
	
	def on_cancel(self):
		frappe.db.set_value("Book Item", self.book_id, "status", "Available")

		res_doc = frappe.get_doc("Reservation", self.reservation_id)
		for row in res_doc.books:
			if row.loan_id == self.loan_id:
				res_doc.remove(row)
		res_doc.save()