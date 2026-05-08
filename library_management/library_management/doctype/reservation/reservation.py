# Copyright (c) 2026, Adil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Reservation(Document):
	def before_save(self):
		self.member_name = frappe.get_doc("Member", self.member_id).full_name
