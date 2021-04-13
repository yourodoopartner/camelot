# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    contact_title = fields.Char(string='Contact Title')
    county = fields.Char(string='County')
    expense = fields.Char(string='ExpenseID')
    fedtax = fields.Char(string='Fed Tax Number')
    person_type_id = fields.Many2one('person.type',string='Person Type')
    vendor_currency_id = fields.Many2one('vendor.currency',string='Vendor Currency')
    customer_currency_id = fields.Many2one('customer.currency',string='Customer Currency')
    vat_no = fields.Char(string='Tax Number')
    alt_contact = fields.Char(string='Alternate Contact')
    tax1_id = fields.Many2one('account.tax',string='Tax1 ID')
    tax2_id = fields.Many2one('account.tax',string='Tax2 ID')
    fax_no = fields.Char(string='Fax Number')
    cie_warehouse = fields.Char(string='Default Cie Warehouse')
    cie_division = fields.Char(string='Default Cie Division')
    account_no = fields.Char(string='Account Number')
    
    store_code_id = fields.Many2one('store.code',string='Store Code')
    type_id = fields.Many2one('customer.type',string='Type')
    group_id = fields.Many2one('customer.group',string='Group')
    warehouse_id = fields.Many2one('customer.whse',string='Whse')
    territory_id = fields.Many2one('customer.territory',string='Territory')
    agent_group_id = fields.Many2one('agent.group',string='Agent Group')
    tax_2_id = fields.Many2one('account.tax',string='Tax 2')
    fedvat = fields.Char(string='Federal ID (VAT)')
    ship_via = fields.Char(string='Ship Via')
    full_name = fields.Char(string='Full Name')
    other_name = fields.Char(string='Other Name')
    
    
    
class PersonType(models.Model):
    _name = 'person.type'   
    _description = 'Person Type'   
    
    name =  fields.Char(string='Type')

class VendorCurrency(models.Model):
    _name = 'vendor.currency' 
    _description = 'Vendor Currency'     
    
    name =  fields.Char(string='Code')
        
class StoreCode(models.Model):
    _name = 'store.code'  
    _description = 'Store Code'    
    
    name =  fields.Char(string='Code')
    
class CustomerType(models.Model):
    _name = 'customer.type'  
    _description = 'Customer Type'    
    
    name =  fields.Char(string='Type')
    
class CustomerGroup(models.Model):
    _name = 'customer.group' 
    _description = 'Customer Group'     
    
    name =  fields.Char(string='Group')    
    
class CustomerWhse(models.Model):
    _name = 'customer.whse'   
    _description = 'Customer Whse'   
    
    name =  fields.Char(string='Whse')   

class CustomerTerritory(models.Model):
    _name = 'customer.territory' 
    _description = 'Customer Territory'   
    
    name =  fields.Char(string='Territory')    
        
class AgentGroup(models.Model):
    _name = 'agent.group'   
    _description = 'Agent Group' 
    
    name =  fields.Char(string='Group')    
             
class CustomerCurrency(models.Model):
    _name = 'customer.currency' 
    _description = 'Customer Currency'     
    
    name =  fields.Char(string='Code')


        