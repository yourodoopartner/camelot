from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    type_id = fields.Many2one('product.type',string='Type')
    selling_period_id = fields.Many2one('selling.period',string='Selling Period')
    collection_id = fields.Many2one('product.collection',string='Collection')
    group_id = fields.Many2one('product.group',string='Group')
    size_code_id = fields.Many2one('product.size',string='Size Code')
    size_id = fields.Many2one('product.size',string='Size')
    cat_id = fields.Many2one('product.cat',string='Cat')
    dim_id = fields.Many2one('product.dim',string='Dim')
    dim_code_id = fields.Many2one('product.dim',string='Dim Code')
    color_id = fields.Many2one('product.color',string='Color')
    color2_id = fields.Many2one('product.color',string='Color2')
    composition_id = fields.Many2one('product.composition',string='Composition')
    whs_id = fields.Many2one('product.whs',string='Whs')
    royalty = fields.Char(string='Royalty')
    made_in_id = fields.Many2one('product.madein',string='Made in')
    origin_id = fields.Many2one('product.origin',string='Origin')
    package_id = fields.Many2one('product.package',string='Package')
    first_cost = fields.Float(string='First Cost')
    retail_price = fields.Float(string='Retail Price')
    color_selling_id = fields.Many2one('color.selling',string='Color Selling Period')
    product_currency_id = fields.Many2one('product.currency',string='Currency')
    current_cost = fields.Float(string='Current Cost')
    
class ProductProduct(models.Model):
    _inherit = 'product.product'

    current_cost = fields.Float(string='Current Cost')
    
class ProductType(models.Model):
    _name = 'product.type'
    _description = 'Product Type'   
    
    name =  fields.Char(string='Type')
    
class SellingPeriod(models.Model):
    _name = 'selling.period'   
    _description = 'Selling Period'
    
    name =  fields.Char(string='Selling Period')   
     
class ProductCollection(models.Model):
    _name = 'product.collection'  
    _description = 'Product Collection' 
    
    name =  fields.Char(string='Collection')
        
class ProductGroup(models.Model):
    _name = 'product.group'  
    _description = 'Product group'  
    
    name =  fields.Char(string='Group')    
    
class ProductSize(models.Model):
    _name = 'product.size'  
    _description = 'Product size'  
    
    name =  fields.Char(string='Size') 

class ProductCat(models.Model):
    _name = 'product.cat'  
    _description = 'Product cat'  
    
    name =  fields.Char(string='Cat')               
  
class ProductDim(models.Model):
    _name = 'product.dim' 
    _description = 'Product dim'   
    
    name =  fields.Char(string='Dim')  
    
class ProductColor(models.Model):
    _name = 'product.color' 
    _description = 'Product color'   
    
    name =  fields.Char(string='Color')  

class ProductComposition(models.Model):
    _name = 'product.composition'   
    _description = 'Product Composition' 
    
    name =  fields.Char(string='Composition')      

class ProductWhs(models.Model):
    _name = 'product.whs'
    _description = 'Product Whs'    
    
    name =  fields.Char(string='Whs')     

class ProductMadeIn(models.Model):
    _name = 'product.madein' 
    _description = 'Product MadeIn'   
    
    name =  fields.Char(string='Made In')   

class ProductOrigin(models.Model):
    _name = 'product.origin' 
    _description = 'Product Origin'   
    
    name =  fields.Char(string='Origin')   
 
class ProductPackage(models.Model):
    _name = 'product.package'
    _description = 'Product Package'    
    
    name =  fields.Char(string='Package') 
    
class ColorSelling(models.Model):
    _name = 'color.selling'  
    _description = 'Color Selling Period'  
    
    name =  fields.Char(string='Color Selling Period')       
    
class ProductCurrency(models.Model):
    _name = 'product.currency'  
    _description = 'Product Currency'  
    
    name =  fields.Char(string='Currency')      
    