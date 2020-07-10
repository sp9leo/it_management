# -*- coding: utf-8 -*-
# Copyright (c) 2019, IT-Geräte und IT-Lösungen wie Server, Rechner, Netzwerke und E-Mailserver sowie auch Backups, and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.data import get_datetime, nowdate
from frappe import _
from frappe.utils import flt

class ITServiceReport(Document):
	def before_save(self):
		if self.timesheet:
			update_timesheet(self)
		else:
			create_timesheet(self)
		update_it_management_table(self)
		'''
		obsolet:
		update_it_ticket_status(self)
		'''
		update_issue_status(self)
			
	def before_submit(self):
		if self.timesheet:
			timesheet = frappe.get_doc("Timesheet", self.timesheet)
			timesheet.submit()
			
	def before_cancel(self):
		if self.timesheet:
			timesheet = frappe.get_doc("Timesheet", self.timesheet)
			timesheet.cancel()

def update_timesheet(self):
	timesheet = frappe.get_doc("Timesheet", self.timesheet)
	timesheet.employee = self.employee
	timesheet.start_date = self.date
	timesheet.end_date = self.date
	'''
	obsolet:
	timesheet.it_ticket = self.it_ticket
	'''
	timesheet.issue = self.issue
	timesheet.note = self.data_14
	timesheet.time_logs = []
	row = timesheet.append('time_logs', {})
	row.activity_type = self.activity_type
	row.from_time = get_datetime(self.date + " " + self.start)
	row.to_time = get_datetime(self.date + " " + self.end)
	row.hours = self.time_total
	row.billable = 1
	row.billing_hours = self.billing_time
	row.project = self.project
	row.task = self.task
	timesheet.save()

def create_timesheet(self):
	timesheet = frappe.get_doc({
		"doctype": "Timesheet",
		"employee": self.employee,
		"start_date": self.date,
		"end_date": self.date,
		#"it_ticket": self.it_ticket,
		"issue": self.issue,
		"note": self.data_14,
		"time_logs": [
			{
				"activity_type": self.activity_type,
				"from_time": get_datetime(self.date + " " + self.start),
				"to_time": get_datetime(self.date + " " + self.end),
				"hours": self.time_total,
				"billable": 1,
				"billing_hours": self.billing_time,
				"project": self.project,
				"task": self.task
			}
		]
	})
	timesheet.insert()
	self.timesheet = timesheet.name
	'''
	obsolet:
	it_ticket = frappe.get_doc("IT Ticket", self.it_ticket)
	it_ticket.add_comment("Comment", self.data_14 or _('Saved Service Report'))
	'''
	issue = frappe.get_doc("Issue", self.issue)
	issue.add_comment("Comment", self.data_14 or _('Saved Service Report'))
	
def update_it_management_table(self):
	for item in self.table_13:
		'''
		obsolet:
		if item.identifier:
			it_ticket = frappe.get_doc("IT Ticket", self.it_ticket)
			for it_ticket_item in it_ticket.it_management_table:
				if it_ticket_item.name == item.identifier:
					it_ticket_item.dynamic_type = item.dynamic_type
					it_ticket_item.dynamic_name = item.dynamic_name
					it_ticket_item.note = item.note
					it_ticket_item.checked = item.checked
					it_ticket.save()
		else:
			it_ticket = frappe.get_doc("IT Ticket", self.it_ticket)
			row = it_ticket.append('it_management_table', {})
			row.dynamic_type = item.dynamic_type
			row.dynamic_name = item.dynamic_name
			row.note = item.note
			row.checked = item.checked
			it_ticket.save()
		'''
		if item.identifier:
			issue = frappe.get_doc("Issue", self.issue)
			for issue_item in issue.it_management_table:
				if issue_item.name == item.identifier:
					issue_item.dynamic_type = item.dynamic_type
					issue_item.dynamic_name = item.dynamic_name
					issue_item.note = item.note
					issue_item.checked = item.checked
					issue.save()
		else:
			issue = frappe.get_doc("Issue", self.issue)
			row = issue.append('it_management_table', {})
			row.dynamic_type = item.dynamic_type
			row.dynamic_name = item.dynamic_name
			row.note = item.note
			row.checked = item.checked
			issue.save()
'''
obsolet:

def update_it_ticket_status(self):
	it_ticket = frappe.get_doc("IT Ticket", self.it_ticket)
	it_ticket.status = self.status
	it_ticket.save()
'''
def update_issue_status(self):
	issue = frappe.get_doc("Issue", self.issue)
	issue.status = self.status
	issue.save()
			
@frappe.whitelist()
def make_sales_invoice(source_name, item_code=None, customer=None):
	target = frappe.new_doc("Sales Invoice")
	timesheet = frappe.get_doc('Timesheet', source_name)
	if timesheet.total_billable_hours:
		if not timesheet.total_billable_hours == timesheet.total_billed_hours:
			hours = flt(timesheet.total_billable_hours) - flt(timesheet.total_billed_hours)
			billing_amount = flt(timesheet.total_billable_amount) - flt(timesheet.total_billed_amount)
			
			target.append('timesheets', {
				'time_sheet': timesheet.name,
				'billing_hours': hours,
				'billing_amount': billing_amount
			})
				
	if customer:
		target.customer = customer

	if item_code:
		target.append('items', {
			'item_code': item_code,
			'qty': hours
		})
		
	target.run_method("calculate_billing_amount_for_timesheet")
	target.run_method("set_missing_values")

	return target
	
@frappe.whitelist()
def fetch_it_management_table_of_issue(issue):
	issue = frappe.get_doc("Issue", issue)
	records = []
	for record in issue.it_management_table:
		if not record.checked:
			records.append({
				'dynamic_type': record.dynamic_type,
				'dynamic_name': record.dynamic_name,
				'note': record.note,
				'name': record.name
			})
	return records
			