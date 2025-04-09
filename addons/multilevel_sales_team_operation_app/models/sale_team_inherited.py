# -*- coding: utf-8 -*-

from odoo import models, fields, exceptions, api, _
from odoo.exceptions import UserError


class CRMTeamInherited(models.Model):
    _inherit = 'crm.team'

    parent_team_id = fields.Many2one('crm.team', string="Parent Team")

    def name_get(self):
        res = []
        for rec in self:
            name = str(rec.name)
            if rec.parent_team_id:
                name = str(rec.parent_team_id.name) + '-' + name
                if rec.parent_team_id.parent_team_id:
                    name = rec.parent_team_id.parent_team_id.name + '-' + name
                    if rec.parent_team_id.parent_team_id.parent_team_id:
                        name = rec.parent_team_id.parent_team_id.parent_team_id.name + '-' + name
                        if rec.parent_team_id.parent_team_id.parent_team_id.parent_team_id:
                            name = rec.parent_team_id.parent_team_id.parent_team_id.parent_team_id.name + '-' + name
            res.append((rec.id, name))
        return res