# Copyright (c) 2026, Adil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Fine(Document):
	def before_save(self):
		if self.rate_per_day < 1:
			frappe.throw("Rate Per Day field must be greater than 0.")
		if self.days_overdue < 1:
			frappe.throw("Days Overdue field must be greater than 0.")
	
		self.total_amount = self.days_overdue * self.rate_per_day 
	
	def on_submit(self):
		if not self.is_paid:
			self.is_paid = True