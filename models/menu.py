response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description

response.menu = []

if auth.user:
    if auth.has_membership("admin"):
        response.menu = [
            ('Szukaj', False, URL('admin', 'index')),
            ('Firmy', False, URL('admin', 'firms')),
            ['Transakcje', False, '',
                [
                    ['Dodaj nową', False, URL('transaction','new')],
                    ['Archiwum Twoich Transakcji', False, URL('transaction','archive')],
                ]
            ],
            ('Przedstawiciele handlowi', False, URL('salesman', 'index')),
            ('Użytkownicy', False, URL('admin', 'users')),
            ['Grupy', False, '',
                [
                    ['Dodaj nową', False, URL('groups', 'new')],
                    ['Zarządzaj przypisaniami', False, URL('groups', 'index')] 
                ]
            ],
            ('Zarządzanie tagami', False, URL('admin', 'field')),
        ]
