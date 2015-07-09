from openerp import models, fields

class procurement_group(models.Model):
    _inherit = 'procurement.group'

    instruction_1 = fields.Char(size=64)
    instruction_2 = fields.Char(size=64)
