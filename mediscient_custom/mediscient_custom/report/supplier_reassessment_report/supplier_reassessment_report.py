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
            "fieldname": "reassessment_period",
            "label": "Reassessment Period",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "fieldname": "reassessment_start_date",
            "label": "Reassessment Start Date",
            "fieldtype": "Date",
            "width": 200
        },
        {
            "fieldname": "next_reassessment_date",
            "label": "Next Reassessment Date",
            "fieldtype": "Date",
            "width": 200
        }
    ]

    # Initialize filter conditions
    filter_conditions = []

    # Dynamically build filter conditions based on user input
    if filters.get("supplier_name"):
        filter_conditions.append(f"`supplier_name` = '{filters['supplier_name']}'")
    
    if filters.get("reassessment_start_date"):
        filter_conditions.append(f"`custom_reassessment_start_date` = '{filters['reassessment_start_date']}'")
    
    if filters.get("next_reassessment_month"):
        month_name = filters["next_reassessment_month"]
        try:
            month_number = datetime.strptime(month_name, "%B").month
            filter_conditions.append(f"MONTH(`custom_next_reassessment_date`) = {month_number}")
        except ValueError:
            frappe.throw("Invalid month name provided for the filter.")
    
    if filters.get("next_reassessment_date"):
        filter_conditions.append(f"`custom_next_reassessment_date` = '{filters['next_reassessment_date']}'")

    # Combine all filter conditions
    filter_conditions_str = " AND ".join(filter_conditions) if filter_conditions else "1=1"

    # Fetch data based on the constructed conditions
    data = frappe.db.sql(f"""
        SELECT 
            `naming_series`,
            `supplier_name`, 
            `custom_reassessment_period`, 
            `custom_reassessment_start_date`, 
            `custom_next_reassessment_date`
        FROM 
            `tabSupplier`
        WHERE 
            {filter_conditions_str}
    """, as_dict=True)

    # Process and enrich data records
    for record in data:
        reassessment_start_date = getdate(record.get("custom_reassessment_start_date"))
        reassessment_period = record.get("custom_reassessment_period", 0)

        # Validate and process reassessment period
        try:
            reassessment_period = int(reassessment_period)
        except (ValueError, TypeError):
            reassessment_period = 0

        # Calculate the next reassessment date if the period is valid
        record["next_reassessment_date"] = (
            add_months(reassessment_start_date, reassessment_period) if reassessment_period else None
        )
        record["reassessment_period"] = reassessment_period
        record["reassessment_start_date"] = reassessment_start_date

    return columns, data
