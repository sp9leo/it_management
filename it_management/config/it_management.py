from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Configuration Management"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Configuration Item",
                    "label": _("Configuration Item"),
                    "description": _("Configuration Item")
                },
                {
                    "type": "doctype",
                    "name": "Solution",
                    "label": _("Solution"),
                    "description": _("Solution")
                },
                {
                    "type": "doctype",
                    "name": "Solution Type",
                    "label": _("Solution Type"),
                    "description": _("Solution Type")
                },
                {
                    "type": "doctype",
                    "name": "Socket",
                    "label": _("Socket"),
                    "description": _("Socket")
                },
                {
                    "type": "doctype",
                    "name": "Network Jack",
                    "label": _("Network Jack"),
                    "description": _("Network Jack")
                },
                {
                    "type": "doctype",
                    "name": "IT Hardware",
                    "label": _("IT Hardware"),
                    "description": _("IT Hardware")
                },
                {
                    "type": "doctype",
                    "name": "IT Backup",
                    "label": _("IT Backup"),
                    "description": _("IT Backup")
                }
            ]
        },
        {
            "label": _("Software"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Licence",
                    "label": _("Licence"),
                    "description": _("Licence")
                },
                {
                    "type": "doctype",
                    "name": "Software Instance",
                    "label": _("Software Instance"),
                    "description": _("Software Instance")
                },
                {
                    "type": "doctype",
                    "name": "User Account",
                    "label": _("User Account"),
                    "description": _("User Account")
                },
                {
                    "type": "doctype",
                    "name": "User Group",
                    "label": _("User Group"),
                    "description": _("User Group")
                },
                {
                    "type": "doctype",
                    "name": "Software Version",
                    "label": _("Software Version"),
                    "description": _("Software Version")
                },
                {
                    "type": "doctype",
                    "name": "IT Software",
                    "label": _("IT Software"),
                    "description": _("IT Software")
                }
            ]
        },
        {
            "label": _("Locations"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Location",
                    "label": _("Location"),
                    "description": _("Location")
                },
                {
                    "type": "doctype",
                    "name": "Address",
                    "label": _("Address"),
                    "description": _("Address")
                },
                {
                    "type": "doctype",
                    "name": "Location Room",
                    "label": _("Location Room"),
                    "description": _("Location Room")
                }
            ]
        },
        {
            "label": _("Network"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Host Domain",
                    "label": _("Host Domain"),
                    "description": _("Host Domain")
                },
                {
                    "type": "doctype",
                    "name": "IP Address",
                    "label": _("IP Address"),
                    "description": _("IP Address")
                },
                {
                    "type": "doctype",
                    "name": "Subnet",
                    "label": _("Subnet"),
                    "description": _("Subnet")
                },
                {
                    "type": "doctype",
                    "name": "Subnet Block",
                    "label": _("Subnet Block"),
                    "description": _("Subnet Block")
                }
            ]
        },
        {
            "label": _("Service"),
            "items": [
                # {
                    # "type": "doctype",
                    # "name": "IT Ticket",
                    # "label": _("IT Ticket"),
                    # "description": _("IT Ticket")
                # },
                {
                    "type": "doctype",
                    "name": "IT Service Report",
                    "label": _("IT Service Report"),
                    "description": _("IT Service Report")
                },
                {
                    "type": "doctype",
                    "name": "Timesheet",
                    "label": _("Timesheet"),
                    "description": _("Timesheet")
                },
                {
                    "type": "doctype",
                    "name": "IT Checklist",
                    "label": _("IT Checklist"),
                    "description": _("IT Checklist")
                }
            ]
        },
        {
            "label": _("Settings"),
            "items": [
                {
                    "type": "doctype",
                    "name": "IT Management Settings",
                    "label": _("Settings"),
                    "description": _("IT Management Settings")
                }
            ]
        }
    ]
