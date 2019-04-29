# coding=utf-8
from mywork.project.odooModule import odooModule
from mywork.project.project import project
from mywork.stocks.gits import gits
from mywork.tools.build_odoo import build_odoo
from mywork.workSpace.store import store


sw = odooModule('builder')

om = build_odoo('builder_module_install', "1.0", git=gits('builder_module_install', url='ssh://kaikong@192.168.31.10/home/git/odoo_builder.git'),newTests=['test11'],oldTests=['odoo11'],
                store=store('kaikong.com.cn'), deploy=['www.kaikong.cn', ],
                depends=[ sw, ])
om.build()
