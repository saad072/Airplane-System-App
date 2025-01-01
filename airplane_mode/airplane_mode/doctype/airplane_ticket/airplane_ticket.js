// Copyright (c) 2024, Saad and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
    before_submit: function(frm) {
        // Check if the status is 'Boarded'
        if (frm.doc.status !== 'Boarded') {
            // Prevent submission and show an error message
            frappe.throw(__('You cannot submit this ticket because the status is not "Boarded".'));
        }
    }
});
