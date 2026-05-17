# Copyright (c) 2026, Adil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import getseries

class Member(Document):
	def autoname(self):
		self.set_name_expression()

	def before_save(self):
		if self.last_name:
			self.full_name = f"{self.first_name} {self.last_name}" 
		else:
			self.full_name = self.first_name

		if self.name:
			self.membership_id = self.name

	# create new Reservation record for this member
	def after_insert(self):
		if self.membership_id:
			doc = frappe.new_doc("Reservation")
			doc.member_id = self.membership_id
			doc.insert()
			
	# delete Reservation record for this member
	def on_trash(self):
		reservation = frappe.db.get_value("Reservation",{"member_id": self.name})

		if reservation:
			frappe.delete_doc("Reservation", reservation)

	def set_name_expression(self):
		# .{first_name}-M.####
		prefix = f"{self.first_name}"
		series = getseries(prefix, 4)
		self.name = f"{prefix}-M{series}"