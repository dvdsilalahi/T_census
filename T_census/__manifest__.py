# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
       'name' : "Census jordan",
       'version': '3.0',
       'description' : """Census""",
       'summary': 'Census',
       'website': 'https://www.odoo.com',
       'author' : "Hamza-Atieh",
       'category' : " People counts",
       'depends' : ['base', 'mail'],
       'data' : ['security/census_security.xml',
                 'security/ir.model.access.csv',
                 'views/census_menu.xml',
                 'views/census_view.xml',
                 'views/nationality_view.xml',
                 ],
       'demo' : [],
       'installable' : True,
       'auto_install':False,
    }

