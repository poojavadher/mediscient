import frappe
from frappe.utils import getdate, add_months
from datetime import datetime

def execute(filters=None):
    # Define report columns with detailed configurations
    columns = [
        {
            "fieldname": "supplier_name",
            "label": "Supplier",
            "fieldtype": "Link",
            "options": "Supplier",
            "width": 200
        },
        {
            "fieldname": "first_evaluation_date",
            "label": "First Evaluation Date",
            "fieldtype": "Date",
            "width": 200
        },
        {
            "fieldname": "reassessment_period",
            "label": "Reassessment Period",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "fieldname": "last_reassessment_date",
            "label": "Last Reassessment Date",
            "fieldtype": "Date",
            "width": 200
        },
        {
            "fieldname": "next_reassessment_date",
            "label": "Next Reassessment Date",
            "fieldtype": "Date",
            "width": 200
        },
        {
            "fieldname": "reminder_date",
            "label": "Reminder Date",
            "fieldtype": "Date",
            "width": 200,
            "hidden":1
        }
    ]

    # Initialize filter conditions
    filter_conditions = []

    # Dynamically build filter conditions based on user input
    if filters.get("supplier_name"):
        filter_conditions.append(f"`supplier_name` = '{filters['supplier_name']}'")
    
    if filters.get("last_reassessment_date"):
        filter_conditions.append(f"`custom_last_reassessment_date` = '{filters['last_reassessment_date']}'")

    if filters.get("first_evaluation_date"):
        filter_conditions.append(f"`custom_first_evaluation_date` = '{filters['first_evaluation_date']}'")
    
    if filters.get("next_reassessment_month"):
        month_name = filters["next_reassessment_month"]
        try:
            month_number = datetime.strptime(month_name, "%B").month
            filter_conditions.append(f"MONTH(`custom_next_reassessment_date`) = {month_number}")
        except ValueError:
            frappe.throw("Invalid month name provided for the filter.")
    
    if filters.get("next_reassessment_date"):
        filter_conditions.append(f"`custom_next_reassessment_date` = '{filters['next_reassessment_date']}'")

    if filters.get("reminder_date"):
        filter_conditions.append(f"`custom_reminder_date` = '{filters['reminder_date']}'")

    # Combine all filter conditions
    filter_conditions_str = " AND ".join(filter_conditions) if filter_conditions else "1=1"

    # Fetch data based on the constructed conditions
    data = frappe.db.sql(f"""
        SELECT 
            `supplier_name`, 
            `custom_reassessment_period`, 
            `custom_last_reassessment_date`, 
            `custom_next_reassessment_date`,
            `custom_first_evaluation_date`,
            `custom_reminder_date`
        FROM 
            `tabSupplier`
        WHERE 
            {filter_conditions_str}
    """, as_dict=True)

    # Process and enrich data records
    for record in data:
        print(data)
        record["next_reassessment_date"] = record.get("custom_next_reassessment_date")
        record["reassessment_period"] = record.get("custom_reassessment_period")
        record["last_reassessment_date"] = record.get("custom_last_reassessment_date")
        record["first_evaluation_date"] = record.get("custom_first_evaluation_date")
        record["reminder_date"] = record.get("custom_reminder_date")

    return columns, data
