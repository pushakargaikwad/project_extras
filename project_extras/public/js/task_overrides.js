frappe.ui.form.on("Task", {
	refresh(frm) {
		frm.set_query("task", "depends_on", () => {
			return {
				filters: {
					name: ["!=", frm.doc.name],
					// removed filtering of tasks only from current project
					// reference to code
					// if (frm.doc.project) filters["project"] = frm.doc.project;
					// source: erpnext/projects/doctype/task/task.js
				},
			};
		});
	},
});
