# Copyright (c) 2026, Adil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BookItem(Document):
	def before_save(self):
		book_id = frappe.get_doc("Book", self.book).name
		self.id = f"{self.name}-{book_id}"
