response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description

response.menu = []

if auth.user:
    if auth.has_membership("admin"):
        response.menu = [
            ('Search', False, URL('admin', 'index')),
            ('Firms', False, URL('admin', 'firms')),
            ('Categories', False, URL('admin', 'category')),
            ('Fields', False, URL('admin', 'field')),
            ('Users', False, URL('admin', 'index')),
        ]