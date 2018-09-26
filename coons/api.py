import frappe
from frappe import _
from frappe.utils import nowdate, add_days, add_months, cstr, cint

@frappe.whitelist()

def update_serial_no(doc, method):

    stock_ledger_entry = frappe.get_doc("Stock Ledger Entry", {"serial_no":("like","%"+doc.name+"%")})

    if(stock_ledger_entry and stock_ledger_entry.voucher_type in ("Purchase Receipt") ):
        purchase_receipt = frappe.get_doc("Purchase Receipt", stock_ledger_entry.voucher_no)
        purchase_receipt_item = frappe.get_doc("Purchase Receipt Item"
            , {"parent": purchase_receipt.name, "serial_no":("like","%"+doc.name+"%")})

        if purchase_receipt_item:
            if cint(purchase_receipt_item.warranty_period_month) > 0:
                doc.warranty_period_month = purchase_receipt_item.warranty_period_month
                doc.amc_expiry_date	= add_months(cstr(purchase_receipt.posting_date),
                    cint(purchase_receipt_item.warranty_period_month))
            else:
                doc.warranty_period_month = 0
                
            doc.save()
