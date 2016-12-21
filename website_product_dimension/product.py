# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2001-2014 Micronaet SRL (<http://www.micronaet.it>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
import os
import sys
from odoo import models, fields, api

class ProductTemplate(models.Model):
    """ Add dimension product
    """
    
    _inherit = 'product.template'
    
    # -------------------------------------------------------------------------
    # TABLE
    # -------------------------------------------------------------------------
    # Dimension:
    height = fields.Char('Height')
    width = fields.Char('Width')
    length = fields.Char('Length')

    pack_h = fields.Char('Pack Height')
    pack_l = fields.Char('Pack Width')
    pack_p = fields.Char('Pack Length')
    
    # Extra:
    q_x_pack = fields.Char('Q. x Pack')
    fabric = fields.Char('Fabric') 
    type_of_material = fields.Char('Type of material')
    vat_price = fields.float ('Vat price')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
