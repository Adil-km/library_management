# Copyright (c) 2026, Adil and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class BookItem(WebsiteGenerator):
		
	def before_validate(self):
		book_id = frappe.get_doc("Book", self.book).name
		if book_id and self.name and not self.id:
			self.id = f"{self.name}-{book_id}"