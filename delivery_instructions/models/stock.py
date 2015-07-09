from openerp import models, fields

class stock_picking(models.Model):
    _inherit = "stock.picking"

    instruction_1 = fields.Char(size=64)
    instruction_2 = fields.Char(size=64)

class stock_move(models.Model):
    _inherit = "stock.move"

    def _prepare_picking_assign(self, cr, uid, move, context=None):
        result = super(stock_move, self)._prepare_picking_assign(cr, uid, move, context=context)
        result.update({
          'instruction_1': move.group_id and move.group_id.instruction_1 or False,
          'instruction_2': move.group_id and move.group_id.instruction_2 or False,
        })
        return result