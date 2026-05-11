# Copyright (c) 2026, Adil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Reservation(Document):
	def before_save(self):
		self.member_name = frappe.get_doc("Member", self.member_id).full_name
	
	def validate(self):
		loans = []
		seen = set()

		for row in self.books:
			if row.loan_id not in seen:
				seen.add(row.loan_id)
				loans.append(row)
		self.books = loans
