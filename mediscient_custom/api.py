import frappe
from frappe.utils import add_months, getdate, today

def update_next_reassessment_dates():
    records = frappe.get_all(
        "Supplier",
        filters={
            "custom_next_reassessment_date": ["<=", today()],
            "custom_reassessment_period": [">", 0] 
        },
        fields=["name", "custom_next_reassessment_date", "custom_reassessment_period"]
    )
    
    for record in records:
        current_date = getdate(record["custom_next_reassessment_date"])
        next_date = add_months(current_date, record["custom_reassessment_period"])
        frappe.db.set_value(
            "Supplier",  
            record["name"],
            "custom_next_reassessment_date",
            next_date
        )
        
    frappe.db.commit() 
