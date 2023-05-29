{
    
      'name' : 'Hotel',
      'sequence':1,
      'author':'Dias Inc.',
      'category': 'Hotel/Hotel',
       'depends': ['base'],
      'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/category_view.xml',
        'views/rooms_view.xml',
        'views/clients_view.xml'
        ],
      'installable': True,
    'application': True

}