from odoo import api, fields, models, _

class wizard_product_data(models.TransientModel):
    _name = 'wizard.product.data'
    _inherit = 'data_import.wizard'

    
    csv_file_name = fields.Char('CSV File Name', size=64)
    csv_file = fields.Binary('Product CSV File', required=True)
    
    
    def upload_product_data(self):
        if self.csv_file:
            list_raw_data = self.get_data_from_attchment(self.csv_file, self.csv_file_name)
            if not list_raw_data:
                raise UserError(_("Cannot import blank sheet."))
            
            for raw in list_raw_data:
                old_data = {}                
                product_id = self.find_product(raw.get('Product',False))
                category_id = self.find_category(raw.get('Class',False))
                type_id = self.find_type(raw.get('Type',False))
                selling_period = self.find_selling_period(raw.get('Selling Period',False))
                color_selling_period = self.find_color_selling_period(raw.get('Color Selling Period',False))
                collection = self.find_collection(raw.get('Collection',False))
                size_code = self.find_size_code(raw.get('Size Code',False))
                size = self.find_size(raw.get('Size',False))
                product_currency = self.find_currency(raw.get('Currency',False))
                dim_code = self.find_dim_code(raw.get('Dim Code',False))
                dim = self.find_dim(raw.get('Dim',False))
                color = self.find_color(raw.get('Color',False))
                color2 = self.find_color2(raw.get('Color2',False))
                whs = self.find_whs(raw.get('Whs',False))
                composition = self.find_composition(raw.get('Composition',False))
                package = self.find_package(raw.get('Package',False))
                origin = self.find_origin(raw.get('Origin',False))
                made_in = self.find_made_in(raw.get('Made in',False))
                cat = self.find_cat(raw.get('Cat',False))
                group = self.find_group(raw.get('Group',False))
                
                old_data['name'] = raw.get('Product',False)
                old_data['description'] = raw.get('Description 1',False)
                old_data['price'] = raw.get('Current Cost',False)
                old_data['standard_price'] = raw.get('Standard Cost',False)
                old_data['list_price'] = raw.get('Selling Price',False)
                old_data['first_cost'] = raw.get('First Cost',False)
                old_data['retail_price'] = raw.get('Retail Price',False)
                old_data['royalty'] = raw.get('Royalty',False)
                old_data['barcode'] = raw.get('Bar Code',False)    
                   
                if not product_id:                             
                    product_id = self.env['product.template'].create(old_data)  
                else:
                    product_id.write(old_data)          
                if not category_id:
                    category_id = self.env['product.category'].create({'name':raw.get('Class',False)})
                    product_id.categ_id = category_id.id
                else:
                    product_id.categ_id = category_id.id
                if not type_id:
                    type_id = self.env['product.type'].create({'name':raw.get('Type',False)})
                    product_id.type_id = type_id.id
                else:
                    product_id.type_id = type_id.id
                if not selling_period:
                    selling_period = self.env['selling.period'].create({'name':raw.get('Selling Period',False)})
                    product_id.selling_period_id = selling_period.id
                else:
                    product_id.selling_period_id = selling_period.id
                if not collection:
                    collection = self.env['product.collection'].create({'name':raw.get('Collection',False)})
                    product_id.collection_id = collection.id
                else:
                    product_id.collection_id = collection.id
                if not size_code:
                    size_code = self.env['product.size'].create({'name':raw.get('Size Code',False)})
                    product_id.size_code_id = size_code.id
                else:
                    product_id.size_code_id = size_code.id
                if not size:
                    size = self.env['product.size'].create({'name':raw.get('Size',False)})
                    product_id.size_id = size.id
                else:
                    product_id.size_id = size.id   
                if not cat:
                    cat = self.env['product.cat'].create({'name':raw.get('Cat',False)})
                    product_id.cat_id = cat.id
                else:
                    product_id.cat_id = cat.id        
                if not dim_code:
                    dim_code = self.env['product.dim'].create({'name':raw.get('Dim Code',False)})
                    product_id.dim_code_id = dim_code.id
                else:
                    product_id.dim_code_id = dim_code.id
                if not dim:
                    dim = self.env['product.dim'].create({'name':raw.get('Dim',False)})
                    product_id.dim_id = dim.id
                else:
                    product_id.dim_id = dim.id   
                if not color:
                    color = self.env['product.color'].create({'name':raw.get('Color',False)})
                    product_id.color_id = color.id
                else:
                    product_id.color_id = color.id      
                if not color2:
                    color2 = self.env['product.color'].create({'name':raw.get('Color2',False)})
                    product_id.color2_id = color2.id
                else:
                    product_id.color2_id = color2.id 
                if not composition:
                    composition = self.env['product.composition'].create({'name':raw.get('Composition',False)})
                    product_id.composition_id = composition.id
                else:
                    product_id.composition_id = composition.id     
                if not whs:
                    whs = self.env['product.whs'].create({'name':raw.get('Whs',False)})
                    product_id.whs_id = whs.id
                else:
                    product_id.whs_id = whs.id  
                if not group:
                    group = self.env['product.group'].create({'name':raw.get('Group',False)})
                    product_id.group_id = group.id
                else:
                    product_id.group_id = group.id                        
                if not made_in:
                    made_in = self.env['product.madein'].create({'name':raw.get('Made in',False)})
                    product_id.made_in_id = made_in.id
                else:
                    product_id.made_in_id = made_in.id   
                if not origin:
                    origin = self.env['product.origin'].create({'name':raw.get('Origin',False)})
                    product_id.origin_id = origin.id
                else:
                    product_id.origin_id = origin.id  
                if not package:
                    package = self.env['product.package'].create({'name':raw.get('Package',False)})
                    product_id.package_id = package.id
                else:
                    product_id.package_id = package.id 
                if not color_selling_period:
                    color_selling_period = self.env['color.selling'].create({'name':raw.get('Color Selling Period',False)})
                    product_id.color_selling_id = color_selling_period.id
                else:
                    product_id.color_selling_id = color_selling_period.id
                if not product_currency:
                    product_currency = self.env['product.currency'].create({'name':raw.get('Currency',False)})
                    product_id.product_currency_id = product_currency.id    
                else:
                    product_id.product_currency_id = product_currency.id   
            return True    
                
    def find_category(self,category):
        category_ids = False
        category_id = self.env['product.category']
        category_ids =  category_id.search([('name','=',category)])
        if category_ids:
            category_ids = category_ids[0]
        return category_ids 
    
    def find_product(self,product):
        product_ids = False
        product_id = self.env['product.template']
        product_ids =  product_id.search([('name','=',product)])
        if product_ids:
            product_ids = product_ids[0]
        return product_ids 
    
    def find_type(self,type):
        type_ids = False
        type_id = self.env['product.type']
        type_ids =  type_id.search([('name','=',type)])
        if type_ids:
            type_ids = type_ids[0]
        return type_ids 
                
    def find_selling_period(self,selling_period):
        period_ids = False
        period_id = self.env['selling.period']
        period_ids =  period_id.search([('name','=',selling_period)])
        if period_ids:
            period_ids = period_ids[0]
        return period_ids             
    
    def find_color_selling_period(self,sell):
        period_ids = False
        period_id = self.env['color.selling']
        period_ids =  period_id.search([('name','=',sell)])
        if period_ids:
            period_ids = period_ids[0]
        return period_ids 
        
    def find_cat(self,cat):
        cat_ids = False
        cat_id = self.env['product.cat']
        cat_ids =  cat_id.search([('name','=',cat)])
        if cat_ids:
            cat_ids = cat_ids[0]
        return cat_ids 
                
    def find_collection(self,collection):
        collection_ids = False
        collection_id = self.env['product.collection']
        collection_ids =  collection_id.search([('name','=',collection)])
        if collection_ids:
            collection_ids = collection_ids[0]
        return collection_ids                 
                
    def find_size_code(self,size):
        size_ids = False
        size_id = self.env['product.size']
        size_ids =  size_id.search([('name','=',size)])
        if size_ids:
            size_ids = size_ids[0]
        return size_ids     
    
    def find_size(self,size):
        size_ids = False
        size_id = self.env['product.size']
        size_ids =  size_id.search([('name','=',size)])
        if size_ids:
            size_ids = size_ids[0]
        return size_ids 
    
    def find_group(self,group):
        group_ids = False
        group_id = self.env['product.group']
        group_ids =  group_id.search([('name','=',group)])
        if group_ids:
            group_ids = group_ids[0]
        return group_ids 
    
    def find_currency(self,currency):
        currency_ids = False
        currency_id = self.env['product.currency']
        currency_ids =  currency_id.search([('name','=',currency)])
        if currency_ids:
            currency_ids = currency_ids[0]
        return currency_ids 
    
    def find_dim_code(self,dim):
        dim_ids = False
        dim_id = self.env['product.dim']
        dim_ids =  dim_id.search([('name','=',dim)])
        if dim_ids:
            dim_ids = dim_ids[0]
        return dim_ids     
    
    def find_dim(self,dim):
        dim_ids = False
        dim_id = self.env['product.dim']
        dim_ids =  dim_id.search([('name','=',dim)])
        if dim_ids:
            dim_ids = dim_ids[0]
        return dim_ids 
    
    def find_color(self,color):
        color_ids = False
        color_id = self.env['product.color']
        color_ids =  color_id.search([('name','=',color)])
        if color_ids:
            color_ids = color_ids[0]
        return color_ids     
    
    def find_color2(self,color):
        color_ids = False
        color_id = self.env['product.color']
        color_ids =  color_id.search([('name','=',color)])
        if color_ids:
            color_ids = color_ids[0]
        return color_ids          
    
    def find_composition(self,comp):
        comp_ids = False
        comp_id = self.env['product.composition']
        comp_ids =  comp_id.search([('name','=',comp)])
        if comp_ids:
            comp_ids = comp_ids[0]
        return comp_ids   
    
    def find_whs(self,whs):
        whs_ids = False
        whs_id = self.env['product.whs']
        whs_ids =  whs_id.search([('name','=',whs)])
        if whs_ids:
            whs_ids = whs_ids[0]
        return whs_ids  
    
    def find_made_in(self,made_in):
        made_in_ids = False
        made_in_id = self.env['product.madein']
        made_in_ids =  made_in_id.search([('name','=',made_in)])
        if made_in_ids:
            made_in_ids = made_in_ids[0]
        return made_in_ids 
    
    def find_origin(self,origin):
        origin_ids = False
        origin_id = self.env['product.origin']
        origin_ids =  origin_id.search([('name','=',origin)])
        if origin_ids:
            origin_ids = origin_ids[0]
        return origin_ids 
    
    def find_package(self,package):
        package_ids = False
        package_id = self.env['product.package']
        package_ids =  package_id.search([('name','=',package)])
        if package_ids:
            package_ids = package_ids[0]
        return package_ids 
    
    
    
    
                   