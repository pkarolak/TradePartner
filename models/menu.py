response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description

response.menu = []

if auth.user:
    if auth.has_membership("admin"):
        response.menu = [
            ('Szukaj', False, URL('app', 'index')),
            ('Firmy', False, URL('app', 'firms')),
            ['Transakcje', False, '',
                [
                    ['Dodaj nową', False, URL('transaction','new')],
                    ['Archiwum Twoich Transakcji', False, URL('transaction','archive')],
                    ['Archiwum Wszystkich Transakcji', False, URL('transaction','archive_all')],
                ]
            ],
            #('Przedstawiciele handlowi', False, URL('salesman', 'index')),
            ('Użytkownicy', False, URL('users', 'list')),
            ['Grupy', False, '',
                [
                    ['Lista grup', False, URL('groups', 'list')],
                    ['Dodaj nową', False, URL('groups', 'new')],
                    ['Zarządzaj przypisaniami', False, URL('groups', 'index')] 
                ]
            ],
            ('Zarządzanie tagami', False, URL('app', 'field')),
        ]
    if auth.has_membership("salesman"):
        response.menu = [
            ('Szukaj', False, URL('app', 'index')),
            ('Firmy', False, URL('app', 'firms')),
            ['Transakcje', False, '',
                [
                    ['Dodaj nową', False, URL('transaction','new')],
                    ['Archiwum Twoich Transakcji', False, URL('transaction','archive')],
                ]
            ],
            #('Przedstawiciele handlowi', False, URL('salesman', 'index')),
            #('Użytkownicy', False, URL('users', 'list')),
            ('Dodaj tagi', False, URL('app', 'field')),
        ]
    if auth.has_membership("visitor"):
        response.menu = [
            ('Szukaj', False, URL('app', 'index')),
        ]