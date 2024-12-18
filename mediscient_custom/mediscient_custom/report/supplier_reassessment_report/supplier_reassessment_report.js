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
			"fieldname": "reassessment_start_date",
			"label": __("Reassessment Start Date"),
			"fieldtype": "Date",
			"default": "",
			"reqd": 0
		},
		{
			"fieldname": "next_reassessment_month",
			"label": __("Next Reassessment Month"),
			"fieldtype": "Select",
			"options": [
				"January", "February", "March", "April", "May", "June",
				"July", "August", "September", "October", "November", "December"
			],
			"default": new Date().toLocaleString('en-us', { month: 'long' }),  // Default to current month
		},
		{
			"fieldname": "next_reassessment_date",
			"label": __("Next Reassessment Date"),
			"fieldtype": "Date",
			"reqd": 0
		}
	]
};
