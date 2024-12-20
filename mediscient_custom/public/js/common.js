frappe.ui.form.on('Supplier', {
    custom_last_reassessment_date: function (frm) {
        if (frm.doc.custom_last_reassessment_date && frm.doc.custom_reassessment_period) {
            const startDate = frappe.datetime.str_to_obj(frm.doc.custom_last_reassessment_date);
            const nextDate = frappe.datetime.add_months(startDate, frm.doc.custom_reassessment_period);
            frm.set_value('custom_next_reassessment_date', frappe.datetime.obj_to_str(nextDate));
        }
    },
    custom_reassessment_period: function (frm) {
        if (frm.doc.custom_last_reassessment_date && frm.doc.custom_reassessment_period) {
            const startDate = frappe.datetime.str_to_obj(frm.doc.custom_last_reassessment_date);
            const nextDate = frappe.datetime.add_months(startDate, frm.doc.custom_reassessment_period);
            frm.set_value('custom_next_reassessment_date', frappe.datetime.obj_to_str(nextDate));
        }
    },
    custom_next_reassessment_date: function (frm) {
        frm.set_value(
            "custom_reminder_date",
            frappe.datetime.add_months(frm.doc.custom_next_reassessment_date, -1)
        );
    }

});
