__author__ = 'one'

from openerp import models, fields, api, _


class Assets(models.Model):
    _name = 'builder.website.asset'

    _rec_name = 'attr_id'
    module_id = fields.Many2one('builder.ir.module.module', 'Module', ondelete='cascade')
    attr_name = fields.Char(string='Name')
    attr_id = fields.Char(string='XML ID', required=True)
    attr_active = fields.Boolean('Active')
    attr_customize_show = fields.Boolean('Customize Show')
    attr_inherit_id = fields.Char('Inherit Asset')
    attr_priority = fields.Integer('Priority')
    type = fields.Selection([
                                ('website.theme', 'website.theme'),
                                ('website.assets_editor', 'website.assets_editor'),
                                ('website.assets_frontend', 'website.assets_frontend'),
                                ('website.assets_backend', 'website.assets_backend'),
    ], 'Type')


class Pages(models.Model):
    _name = 'builder.website.page'

    _rec_name = 'attr_name'

    module_id = fields.Many2one('builder.ir.module.module', 'Module', ondelete='cascade')
    attr_name = fields.Char(string='Name', required=True)
    attr_id = fields.Char('XML ID', required=True)
    attr_inherit_id = fields.Char('Inherit Asset')
    attr_priority = fields.Integer('Priority')
    attr_page = fields.Boolean('Page', default=True)
    wrap_layout = fields.Selection([
        ('website.layout', 'website.layout'),
        ('web.login_layout', 'web.login_layout'),
    ], default='website.layout')
    content = fields.Text('Body')


class Theme(models.Model):
    _name = 'builder.website.theme'

    _rec_name = 'attr_name'

    module_id = fields.Many2one('builder.ir.module.module', 'Module', ondelete='cascade')
    attr_name = fields.Char(string='Name')
    attr_description = fields.Char('Description')
    attr_id = fields.Char('XML ID')
    asset_ref = fields.Char('Asset')
    asset_id = fields.Many2one('builder.website.asset', 'Asset')
    asset_selection_type = fields.Selection([('module', 'Module'), ('system', 'System')], 'Type', required=True)


class Menu(models.Model):
    _name = 'builder.website.menu'

    _order = 'sequence, id'

    module_id = fields.Many2one('builder.ir.module.module', 'Module', ondelete='cascade')
    sequence = fields.Integer('Sequence')
    name = fields.Char(string='Name', required=True)
    url = fields.Char("URL")
    page_id = fields.Many2one('builder.website.page')
    target_type = fields.Selection([('module', 'Module'), ('system', 'System')], 'Type', required=True)
    parent_id = fields.Many2one('builder.website.menu', 'Parent')


class Module(models.Model):
    _inherit = 'builder.ir.module.module'

    website_menu_ids = fields.One2many('builder.website.menu', 'module_id', 'Menu')
    website_asset_ids = fields.One2many('builder.website.asset', 'module_id', 'Assets')
    website_theme_ids = fields.One2many('builder.website.theme', 'module_id', 'Themes')
    website_page_ids = fields.One2many('builder.website.page', 'module_id', 'Pages')