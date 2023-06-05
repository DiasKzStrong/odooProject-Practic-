{
    
      'name' : 'Hotel',
      'sequence':1,
      'author':'Dias Inc.',
      'category': 'Hotel/Hotel',
       'depends': ['mail'],
      'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/category_view.xml',
        'views/rooms_view.xml',
        'views/clients_view.xml',
        'views/services_view.xml',
        'views/category_services_view.xml',
        'views/clients_services.xml',
        'views/clients_payment.xml',
        'views/clientsroom.xml',
        'views/invoice.xml'
        ],
      'installable': True,
    'application': True
    
}