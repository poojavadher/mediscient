frappe.ui.form.on('Supplier', {
    custom_reassessment_start_date: function (frm) {
        if (frm.doc.custom_reassessment_start_date && frm.doc.custom_reassessment_period) {
            const startDate = frappe.datetime.str_to_obj(frm.doc.custom_reassessment_start_date);
            const nextDate = frappe.datetime.add_months(startDate, frm.doc.custom_reassessment_period);
            frm.set_value('custom_next_reassessment_date', frappe.datetime.obj_to_str(nextDate));
        }
    },
});
