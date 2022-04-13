from odoo import http
from odoo.http import request

class messurement(http.Controller):
	
    @http.route(['/messurements/<model("messurement_vialeta.type"):vialeta>'], auth='public', website=True)
    def fun_vialeta(self, vialeta):
            return http.request.render('messurement.vialeta',{
                "vialeta": vialeta
            
            })
        
        
           # @http.route('/messurement/', website=True, auth='public')
    #def messurement_vialeta(self, **kw):
        #return "hello world"
     #   return request.render("messurement.vialeta_page",{})