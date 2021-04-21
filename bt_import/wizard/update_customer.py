
from odoo import api, fields, models, _

class wizard_company_data(models.TransientModel):
    _name = 'wizard.customer.data'
    _inherit = 'data_import.wizard'

    
    csv_file_name = fields.Char('CSV File Name', size=64)
    csv_file = fields.Binary('Supplier CSV File', required=True)
    cust_csv_file_name = fields.Char('CSV File Name', size=64)
    cust_csv_file = fields.Binary('Customer CSV File', required=True)
    
    def upload_customer_data(self):
        if self.csv_file:
            list_raw_data = self.get_data_from_attchment(self.csv_file, self.csv_file_name)
            if not list_raw_data:
                raise UserError(_("Cannot import blank sheet."))
            
            #supplier data import
            for raw in list_raw_data:
                old_data = {}
                
                if raw.get('Country') == 'United States Of America' or 'UNITED STATES OF AMERICA' or 'U.S.A.':
                    country = self.env['res.country'].search([('name','=','United States')]) 
                else:
                    country = self.env['res.country'].search([('name','=',raw.get('Country',False))])    
                state = self.env['res.country.state'].search([('code','=',raw.get('State',False)),('country_id','=',country.id)])
                customer_id = self.find_supplier(raw.get('Company Name',False))
                tax1_id = self.find_tax1(raw.get('Tax1ID',False))
                tax2_id = self.find_tax2(raw.get('Tax2ID',False))
                bank_id = self.find_bank(raw.get('AccountNumber'))
                contact_id = self.find_contact(raw.get('ContactName'))
                term_id = self.find_term(raw.get('TermId'))
                type_id = self.find_person_type(raw.get('PersonTypeID'))
                vendor_currency_id = self.find_currency(raw.get('Currency_Id'))
                
                old_data['ref'] = raw.get('VendorCode',False)
                old_data['name'] = raw.get('Company Name',False)
                old_data['supplier_rank'] = 1
                old_data['customer_rank'] = 0
                old_data['street'] = raw.get('Address',False)
                old_data['street2'] = raw.get('Address2',False)
                old_data['city'] = raw.get('City',False)
                old_data['zip'] = raw.get('Zip',False)                  
                old_data['country_id'] = country.id or False
                old_data['state_id'] = state.id or False
                old_data['phone'] = raw.get('PhoneNumber',False)
                old_data['vat'] = raw.get('TaxNumber',False)
                old_data['vat_no'] = raw.get('TaxNumber2',False)
                old_data['credit_limit'] = raw.get('CreditLimit',False)
                old_data['alt_contact'] = raw.get('AltContact',False)
                old_data['comment'] = raw.get('Notes',False)
                old_data['contact_title'] = raw.get('ContactTitle',False)
                old_data['county'] = raw.get('County',False)
                old_data['expense'] = raw.get('ExpenseID',False)
                old_data['fedtax'] = raw.get('FedTaxNumber',False)
                old_data['fax_no'] = raw.get('FaxNumber',False)
                old_data['cie_warehouse'] = raw.get('DefaultCieWarehouseID',False)
                old_data['cie_division'] = raw.get('DefaultCieDivisionID',False)
                old_data['account_no'] = raw.get('AccountNumber',False)
                    
                customer_id = self.env['res.partner'].create(old_data)
                if not tax1_id :
                    tax1_id = self.env['account.tax'].create({'name':raw.get('Tax1ID',False),'amount':0})                        
                    customer_id.tax1_id = tax1_id.id
                else:
                    customer_id.tax1_id = tax1_id.id
                if not tax2_id:
                    if raw.get('Tax2ID',False) == 'PSTP':
                        tax2_id = self.env['account.tax'].create({'name':raw.get('Tax2ID',False),'amount':0})
                    customer_id.tax2_id = tax2_id.id
                else:
                    customer_id.tax2_id = tax2_id.id 
                if not term_id:
                    term_id = self.env['account.payment.term'].create({'name':raw.get('TermId',False)})
                    customer_id.property_supplier_payment_term_id = term_id.id    
                else:
                    customer_id.property_supplier_payment_term_id = term_id.id  
                if not type_id:
                    type_id = self.env['person.type'].create({'name':raw.get('PersonTypeID',False)})
                    customer_id.person_type_id = type_id.id    
                else:
                    customer_id.person_type_id = type_id.id           
                if not contact_id:
                    contact_id = self.env['res.partner'].create({'name':raw.get('ContactName',False),'parent_id':customer_id.id})
                    customer_id.child_ids.name = contact_id.name
                else:
                    customer_id.child_ids.name = contact_id.name
                if not vendor_currency_id:
                    vendor_currency_id = self.env['vendor.currency'].create({'name':raw.get('Currency_Id',False)})
                    customer_id.vendor_currency_id = vendor_currency_id.id    
                else:
                    customer_id.vendor_currency_id = vendor_currency_id.id         
                        
                  
                        
            
         #customer data import            
        if self.cust_csv_file:  
            list_raw_customer_data = self.get_data_from_attchment(self.cust_csv_file, self.cust_csv_file_name)        
            for raw in list_raw_customer_data:
                old_data = {}
                if raw.get('Country') == 'United States Of America' or 'UNITED STATES OF AMERICA' or 'U.S.A.':
                    country = self.env['res.country'].search([('name','=','United States')]) 
                else:
                    country = self.env['res.country'].search([('name','=',raw.get('Country',False))])    
                state = self.env['res.country.state'].search([('code','=',raw.get('State',False)),('country_id','=',country.id)])
                customer_id = self.find_customer(raw.get('Company Name',False))
                type_id = self.find_type(raw.get('Type'))
                tax_2_id = self.find_tax_2(raw.get('Tax 2'))
                term_id = self.find_terms(raw.get('Terms'))
                store_id = self.find_store_code(raw.get('Store Code'))
                whse_id = self.find_whse(raw.get('Whse'))   
                territory_id = self.find_territory(raw.get('Territory'))                      
                group_id = self.find_group(raw.get('Group'))
                agent_group_id = self.find_agent_group(raw.get('Agent Group'))
                customer_currency_id = self.find_currency(raw.get('Currency'))
                parent_id = self.find_company_contact(raw.get('Customer')) 
                
                          
                old_data['name'] = raw.get('Company Name',False)
                old_data['customer_rank'] = 1
                old_data['supplier_rank'] = 0
                old_data['street'] = raw.get('Address1',False)
                old_data['street2'] = raw.get('Address2',False)
                old_data['city'] = raw.get('City',False)
                old_data['zip'] = raw.get('Zip Code',False)                  
                old_data['country_id'] = country.id or False
                old_data['state_id'] = state.id or False
                old_data['phone'] = raw.get('Phone',False)
                old_data['email'] = raw.get('Email',False)
                old_data['vat'] = raw.get('Tax 1',False)
                old_data['fedvat'] = raw.get('Federal ID (VAT)',False)
                old_data['ship_via'] = raw.get('Ship Via',False)
                old_data['full_name'] = raw.get('Full Name',False)
                old_data['other_name'] = raw.get('Other Names',False)   
                

                customer_id = self.env['res.partner'].create(old_data) 
                if not parent_id:    
                    parent = self.env['res.partner'].create({'name':raw.get('Customer',False)}) 
                    customer_id.parent_id = parent.id  
                else:             
                    customer_id.parent_id = parent_id.id                      
                if not tax_2_id:
                    tax_2_id = self.env['account.tax'].create({'name':raw.get('Tax 2',False),'amount':0})
                    customer_id.tax_2_id = tax_2_id.id
                else:
                    customer_id.tax_2_id = tax_2_id.id  
                if not store_id:
                    store_id = self.env['store.code'].create({'name':raw.get('Store Code',False)})
                    customer_id.store_code_id = store_id.id
                else:
                    customer_id.store_code_id = store_id.id   
                if not type_id:
                    type_id = self.env['customer.type'].create({'name':raw.get('Type',False)})
                    customer_id.type_id = type_id.id
                else:
                    customer_id.type_id = type_id.id           
                if not group_id:
                    group_id = self.env['customer.group'].create({'name':raw.get('Group',False)})
                    customer_id.group_id = group_id.id
                else:
                    customer_id.group_id = group_id.id
                if not whse_id:
                    whse_id = self.env['customer.whse'].create({'name':raw.get('Whse',False)})
                    customer_id.warehouse_id = whse_id.id
                else:
                    customer_id.warehouse_id = whse_id.id    
                if not agent_group_id:
                    agent_group_id = self.env['agent.group'].create({'name':raw.get('Agent Group',False)})
                    customer_id.agent_group_id = agent_group_id.id
                else:
                    customer_id.agent_group_id = agent_group_id.id    
                if not territory_id:
                    territory_id = self.env['customer.territory'].create({'name':raw.get('Territory',False)})
                    customer_id.territory_id = territory_id.id
                else:
                    customer_id.territory_id = territory_id.id                            
                if not term_id:
                    term_id = self.env['account.payment.term'].create({'name':raw.get('Terms',False)})
                    customer_id.property_payment_term_id = term_id.id    
                else:
                    customer_id.property_payment_term_id = term_id.id  
                if not customer_currency_id:
                    customer_currency_id = self.env['customer.currency'].create({'name':raw.get('Currency',False)})
                    customer_id.customer_currency_id = customer_currency_id.id    
                else:
                    customer_id.customer_currency_id = customer_currency_id.id       
               
    
        return True
    
    def find_contact(self,name):
        contact_ids = False
        contact_id = self.env['res.partner']
        contact_ids =  contact_id.search([('name','=',name)])
        if contact_ids:
            contact_ids = contact_ids[0]
        return contact_ids 
    
    def find_company_contact(self,name):
        contact_ids = False
        contact_id = self.env['res.partner']
        contact_ids =  contact_id.search([('name','=',name)])
        if contact_ids:
            contact_ids = contact_ids[0]
        return contact_ids 
    
    def find_term(self,term):
        term_ids = False
        term_id = self.env['account.payment.term']
        term_ids =  term_id.search([('name','=',str(term))])
        if term_ids:
            term_ids = term_ids[0]
        return term_ids
    
    def find_terms(self,term):
        term_ids = False
        term_id = self.env['account.payment.term']
        term_ids =  term_id.search([('name','=',str(term))])
        if term_ids:
            term_ids = term_ids[0]
        return term_ids
    
    def find_bank(self,acc_number):
        bank_ids = False
        bank_id = self.env['res.partner.bank']
        bank_ids =  bank_id.search([('acc_number','=',acc_number)])
        if bank_ids:
            bank_ids = bank_ids[0]
        return bank_ids 
    
    def find_tax1(self,tax):
        tax_ids = False
        tax_id = self.env['account.tax']
        tax_ids =  tax_id.search([('name','=',tax)])
        if tax_ids:
            tax_ids = tax_ids[0]
        return tax_ids  
    
    def find_tax2(self,tax):
        tax_ids = False
        tax_id = self.env['account.tax']
        tax_ids =  tax_id.search([('name','=',tax)])
        if tax_ids:
            tax_ids = tax_ids[0]
        return tax_ids    

    def find_person_type(self,type):
        type_ids = False
        type_id = self.env['person.type']
        type_ids =  type_id.search([('name','=',type)])
        if type_ids:
            type_ids = type_ids[0]
        return type_ids    
    
    def find_supplier(self,supplier):
        supplier_ids = False
        supplier_id = self.env['res.partner']
        supplier_ids =  supplier_id.search([('supplier_rank','=',1),('name','=',supplier)])
        if supplier_ids:
            supplier_ids = supplier_ids[0]
        return supplier_ids     
    
    def find_customer(self,customer):
        supplier_ids = False
        supplier_id = self.env['res.partner']
        supplier_ids =  supplier_id.search([('customer_rank','=',1),('name','=',customer)])
        if supplier_ids:
            supplier_ids = supplier_ids[0]
        return supplier_ids  
    
    
    def find_agent_group(self,agent_group):
        group_ids = False
        group_id = self.env['agent.group']
        group_ids =  group_id.search([('name','=',agent_group)])
        if group_ids:
            group_ids = group_ids[0]
        return group_ids           
    
    def find_group(self,group):
        group_ids = False
        group_id = self.env['customer.group']
        group_ids =  group_id.search([('name','=',group)])
        if group_ids:
            group_ids = group_ids[0]
        return group_ids    
        
    def find_store_code(self,store_code):
        store_ids = False
        store_id = self.env['store.code']
        store_ids =  store_id.search([('name','=',store_code)])
        if store_ids:
            store_ids = store_ids[0]
        return store_ids   
    
    def find_type(self,type):
        type_ids = False
        type_id = self.env['customer.type']
        type_ids =  type_id.search([('name','=',type)])
        if type_ids:
            type_ids = type_ids[0]
        return type_ids   
    
    def find_whse(self,whse):
        whse_ids = False
        whse_id = self.env['customer.whse']
        whse_ids =  whse_id.search([('name','=',whse)])
        if whse_ids:
            whse_ids = whse_ids[0]
        return whse_ids  
    
    def find_territory(self,territory):
        territory_ids = False
        territory_id = self.env['customer.whse']
        territory_ids =  territory_id.search([('name','=',territory)])
        if territory_ids:
            territory_ids = territory_ids[0]
        return territory_ids  
    
    def find_tax_2(self,tax2):
        tax2_ids = False
        tax2_id = self.env['account.tax']
        tax2_ids =  tax2_id.search([('name','=',tax2)])
        if tax2_ids:
            tax2_ids = tax2_ids[0]
        return tax2_ids  
    
    def find_currency(self,currency):
        currency_ids = False
        currency_id = self.env['vendor.currency']
        currency_ids =  currency_id.search([('name','=',currency)])
        if currency_ids:
            currency_ids = currency_ids[0]
        return currency_ids  
    
    def find_currency(self,currency):
        currency_ids = False
        currency_id = self.env['customer.currency']
        currency_ids =  currency_id.search([('name','=',currency)])
        if currency_ids:
            currency_ids = currency_ids[0]
        return currency_ids 
    
    
    
    