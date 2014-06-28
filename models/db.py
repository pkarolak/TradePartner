db = DAL("sqlite://storage.sqlite")

response.generic_patterns = ['*'] if request.is_local else []
response.optimize_css = 'concat,minify,inline'
response.optimize_js = 'concat,minify,inline'
response.static_version = '1.0.0'

from gluon.tools import Auth, Crud, Service, PluginManager, Mail, prettydate
auth = Auth(db)
auth.define_tables(username=False)
crud = Crud(db)

auth.settings.extra_fields['auth_user'] = (
    [Field('user_type', requires=IS_IN_SET(['admin', 'salesman', 'designer', 'other']))]
)

auth.settings.login_next = URL('index')
auth.settings.register_next = URL('user', args='login')
auth.settings.register_onaccept.append(lambda form: auth.add_membership('other', db(db.auth_user.email == form.vars.email).select().first().id))
auth.settings.create_user_groups = False

db.auth_user._format = '%(first_name)s %(last_name)s'

db.define_table(
    'fields',
    Field('name'),
    format = '%(name)s'
)
db.fields.name.requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'fields.name')]
db.fields.name.label = T('Element oferty')

db.define_table('firms',
    Field('name'),
    Field('address'),
    Field('city'),
    Field('zip'),
    Field('nip', unique = True),
    Field('website'),
    Field('email'),
    Field('phone'),
    Field('categories', 'list:reference fields'),
    Field('rating', 'integer', default=0),
    format = '%(name)s'
)

db.firms.name.requires = IS_NOT_EMPTY()
db.firms.nip.requires = IS_NOT_EMPTY()
db.firms.email.requires = [IS_EMAIL(), IS_NOT_IN_DB(db, 'firms.email')]
db.firms.phone.requires = IS_NOT_EMPTY()
db.firms.ondelete = 'CASCADE'
db.firms.onupdate = 'CASCADE'
db.firms.categories.widget = SQLFORM.widgets.checkboxes.widget
db.firms.name.label = T('Nazwa')
db.firms.address.label = T('Adres')
db.firms.city.label = T('Miasto')
db.firms.zip.label = T('Kod pocztowy')
db.firms.website.label = T('Strona internetowa')
db.firms.email.label = T('Email')
db.firms.phone.label = T('Nr telefonu')
db.firms.categories.label = T('Oferta')
db.firms.rating.label = T('Ocena')


db.define_table('representatives',
    Field('firm_id',db.firms),
    Field('name'),
    Field('surname'),
    Field('email'),
    Field('phone'),
    format = '%(name)s %(surname)s'
)
db.representatives.name.requires = IS_NOT_EMPTY()
db.representatives.surname.requires = IS_NOT_EMPTY()
db.representatives.email.requires = IS_EMAIL()
db.representatives.phone.requires = IS_NOT_EMPTY()
db.representatives.firm_id.label = T('Firma')
db.representatives.name.label = T('Imię')
db.representatives.surname.label = T('Nazwisko')
db.representatives.email.label = T('Email')
db.representatives.phone.label = T('Telefon')


db.define_table('comments',
    Field('firm_id', db.firms),
    Field('outer_representative_id', db.representatives),
    Field('self_representative_id', db.auth_user),
    Field('comment', 'text', requires=IS_NOT_EMPTY()),
    Field('date','datetime', requires=IS_DATETIME()),
)
db.comments.firm_id.label = T('Firma')
db.comments.outer_representative_id.label = T('Przedstawiciel firmy')
db.comments.self_representative_id.label = T('Komentujący')
db.comments.comment.label = T('Komentarz')


db.define_table('transactions',
    Field('firm_id', db.firms),
    Field('outer_representative_id', db.representatives),
    Field('self_representative_id', db.auth_user),
    Field('description', 'text', requires=IS_NOT_EMPTY()),
    Field('comment', 'text'),
    Field('transaction_date', 'date', requires=IS_NOT_EMPTY()),
)
db.transactions.firm_id.label = T('Firma')
db.transactions.outer_representative_id.label = T('Przedstawiciel firmy')
db.transactions.self_representative_id.label = T('Zamawiający')
db.transactions.description.label = T('Opis zamowienia')
db.transactions.comment.label = T('Komentarz')
db.transactions.transaction_date.label = T('Data zamówienia')

db.define_table('likes',
    Field('firm_id', db.firms),
    Field('liker', db.auth_user),
)
db.likes.liker.requires=IS_NOT_IN_DB(db(db.likes.firm_id==request.vars.firm_id), 'likes.liker')
db.likes.firm_id.label = T('Firma')
db.likes.liker.label = T('Lubi ją')
db.auth_user.first_name.label = T('Imię')
db.auth_user.last_name.label = T('Nazwisko')

db.auth_membership.user_id.label = T('User ID')
db.auth_membership.group_id.label = T('Group ID')
