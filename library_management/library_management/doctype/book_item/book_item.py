# Copyright (c) 2026, Adil and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class BookItem(WebsiteGenerator):
	def before_save(self):
		book_id = frappe.get_doc("Book", self.book).name
		self.id = f"{self.name}-{book_id}"
