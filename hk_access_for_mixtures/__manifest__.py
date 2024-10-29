{
    "name": "Control access to mixtures",
    "version": "17.0.1.0.0",
    "category": "Category",
    "license": "OPL-1",
    "author": "HOTKEY Company",
    "maintainers": ["HOTKEY Company"],
    "website": "https://hotkey.ua",
    "depends": ['base', 'product', 'stock', 'mrp'],
    "external_dependencies": {"python": []},
    "data": [
        "security/group.xml",
        'security/ir.model.access.csv',
        'views/product_access.xml',
        'views/product_template.xml',
        'views/mrp_production.xml',
        'report/mo_report.xml',
    ],
    "qweb": [],
    "installable": True,
}
