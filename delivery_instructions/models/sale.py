from openerp import models, fields

class sale_order(models.Model):
    _inherit = "sale.order"

    instruction_1 = fields.Char(size=64)
    instruction_2 = fields.Char(size=64)

    def _prepare_procurement_group(self, cr, uid, order, context=None):
        res = super(sale_order, self)._prepare_procurement_group(cr, uid, order, context=None)
        res.update({
          'instruction_1': order.instruction_1,
          'instruction_2': order.instruction_2,
          })
        return res