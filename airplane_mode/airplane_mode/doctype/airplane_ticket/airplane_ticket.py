import frappe
from frappe.model.document import Document
class AirplaneTicket(Document):
    def before_save(self):
        # Ensure each add-on is unique in the add_ons child table
        self.remove_duplicate_add_ons()
        # Calculate total add-ons amount
        total_add_ons = 0.0
        for add_on in self.add_ons:
            total_add_ons += add_on.amount or 0
        # Calculate total amount (flight price + add-ons)
        self.total_amount = total_add_ons + (self.flight_price or 0)
        # Ensure only boarded tickets can be updated
        if not self.status == "Boarded":
            frappe.throw ("Only boarded tickets can be updated.")
        else:
            pass
    def remove_duplicate_add_ons(self):
        """Remove duplicate add-ons from the child table."""
        unique_add_ons = {}
        cleaned_add_ons = []
        for add_on in self.add_ons:
            # Use the item field as the unique identifier
            if add_on.item not in unique_add_ons:
                unique_add_ons[add_on.item] = True
                cleaned_add_ons.append(add_on)
        # Replace the add_ons child table with the cleaned list
        self.add_ons = cleaned_add_ons






