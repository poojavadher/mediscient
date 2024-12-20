frappe.query_reports["Supplier Reassessment Report"] = {
	"filters": [
		{
			"fieldname": "supplier_name",
			"label": __("Supplier"),
			"fieldtype": "Link",
			"options": "Supplier",
			"default": "",
			"reqd": 0
		},
		{
			"fieldname": "last_reassessment_date",
			"label": __("Last Reassessment Date"),
			"fieldtype": "Date",
			"default": "",
			"reqd": 0
		},
		{
			"fieldname": "first_evaluation_date",
			"label": __("First Evaluation Date"),
			"fieldtype": "Date",
			"default": "",
			"reqd": 0
		},
		{
			"fieldname": "next_reassessment_month",
			"label": __("Next Reassessment Month"),
			"fieldtype": "Select",
			"options": [
				"", "January", "February", "March", "April", "May", "June",
				"July", "August", "September", "October", "November", "December"
			],
			"default": new Date().toLocaleString('en-us', { month: 'long' }),  // Default to current month
		},
		{
			"fieldname": "next_reassessment_date",
			"label": __("Next Reassessment Date"),
			"fieldtype": "Date",
			"reqd": 0
		},
		{
			"fieldname": "reminder_date",
			"label": __("Reminder Date"),
			"fieldtype": "Date",
			"hidden": 1
		}
	]
};
