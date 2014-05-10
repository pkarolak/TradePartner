db = DAL("sqlite://storage.sqlite")

from gluon.tools import Auth, Crud
auth = Auth(db)
auth.define_tables(username=True)
crud = Crud(db)

auth.settings.extra_fields['auth_user'] = (
    [Field('user_type', requires=IS_IN_SET(['admin', 'salesman', 'designer', 'other']))]
)

auth.settings.login_next = URL('index')
auth.settings.register_next = URL('user', args='login')
auth.settings.register_onaccept.append(lambda form: auth.add_membership('other', db(db.auth_user.email == form.vars.email).select().first().id))


db.define_table('firm',
    Field('name'),
    Field('address'),
    Field('city'),
    Field('zip'),
    Field('nip', unique = True),
    Field('website'),
    Field('email'),
    Field('phone'),
    format = '%(name)s'
)
db.firm.name.requires = IS_NOT_EMPTY()
db.firm.nip.requires = IS_NOT_EMPTY()
db.firm.email.requires = [IS_EMAIL(), IS_NOT_IN_DB(db, 'firm.email')]
db.firm.phone.requires = IS_NOT_EMPTY()
db.firm.ondelete = 'CASCADE'
db.firm.onupdate = 'CASCADE'


db.define_table('representative',
    Field('firm_id',db.firm),
    Field('name'),
    Field('surname'),
    Field('email'),
    Field('phone'),
    format = '%(name)s %(surname)s'
)
db.representative.name.requires = IS_NOT_EMPTY()
db.representative.surname.requires = IS_NOT_EMPTY()
db.representative.email.requires = IS_EMAIL()
db.representative.phone.requires = IS_NOT_EMPTY()


db.define_table(
    'category',
    Field('name'),
    format = '%(name)s'
)
db.category.name.requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'category.name')]

db.define_table(
    'field',
    Field('name'),
    Field('category', db.category, notnull=True),
    format = '%(name)s'
)
db.field.name.requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'field.name')]

db.define_table(
    'firms_fields',
    Field('firm_id', db.firm),
    Field('field_id', db.field),
    format = '%(firm_id)s %(filed_id)s'
)