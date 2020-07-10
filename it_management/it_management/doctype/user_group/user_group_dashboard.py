from __future__ import unicode_literals
from frappe import _


def get_data():
    return {
        'fieldname': 'user_group',
        'non_standard_fieldnames': {
            #'IT Ticket': 'dynamic_name'
			'Issue': 'dynamic_name'
        },
        'transactions': [
            {
                'label': _('Service'),
                'items': ['Issue', 'User Account']#IT Ticket']
            }
        ]
    }
