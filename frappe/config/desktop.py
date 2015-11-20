from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"Activity": {
			"color": "#333333",
			"icon": "icon-play",
			"icon": "octicon octicon-pulse",
			"label": _("Activity"),
			"link": "activity",
			"type": "page"
		},
		"Calendar": {
			"color": "#333333",
			"icon": "icon-calendar",
			"icon": "octicon octicon-calendar",
			"label": _("Calendar"),
			"link": "Calendar/Event",
			"type": "view"
		},
		"Messages": {
			"color": "#333333",
			"icon": "icon-comments",
			"icon": "octicon octicon-comment-discussion",
			"label": _("Messages"),
			"link": "messages",
			"type": "page"
		},
		"To Do": {
			"color": "#333333",
			"icon": "icon-check",
			"icon": "octicon octicon-check",
			"label": _("To Do"),
			"link": "List/ToDo",
			"doctype": "ToDo",
			"type": "list"
		},
		"Notes": {
			"color": "#333333",
			"doctype": "Note",
			"icon": "icon-file-alt",
			"icon": "octicon octicon-file-text",
			"label": _("Notes"),
			"link": "List/Note",
			"type": "list"
		},
		"Website": {
			"color": "#333333",
			"icon": "icon-globe",
			"icon": "octicon octicon-globe",
			"type": "module"
		},
		"Installer": {
			"color": "#333333",
			"icon": "icon-download",
			"icon": "octicon octicon-cloud-download",
			"link": "applications",
			"type": "page",
			"label": _("Installer")
		},
		"Setup": {
			"color": "#333333",
			"icon": "icon-wrench",
			"icon": "octicon octicon-settings",
			"type": "module"
		},
		"Core": {
			"color": "#333333",
			"icon": "icon-cog",
			"icon": "octicon octicon-file-binary",
			"type": "module",
			"system_manager": 1
		},
		"Integrations": {
			"color": "#333333",
			"icon": "octicon octicon-plug",
			"type": "module",
			"system_manager": 1
		}
	}
