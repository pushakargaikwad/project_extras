import frappe
from frappe.desk.calendar import get_events as original_get_events

# Patch based on upstream fix (not yet merged at time of writing):
# https://github.com/AhmedAbokhatwa/frappe/commit/07b1f3b0892c4351c82d64267baa92a580630631

@frappe.whitelist()
def get_events(*args, **kwargs):
    kwargs.pop("cmd", None)

    events = original_get_events(*args, **kwargs)

    # Apply ONLY for Task doctype
    if kwargs.get("doctype") != "Task":
        return events

    for event in events:
        start = event.get("start")
        end = event.get("end")

        # ensure datetime-like strings are preserved
        if isinstance(start, str) and " " in start:
            event["start"] = start
        if isinstance(end, str) and " " in end:
            event["end"] = end

        # force non all-day
        event["allDay"] = False

    return events