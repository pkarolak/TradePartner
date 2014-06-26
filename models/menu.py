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
            ('Użytkownicy', False, URL('admin', 'users')),
            ('Grupy', False, URL('admin', 'groups')),
            ('Zarządzanie tagami', False, URL('admin', 'field')),
        ]
