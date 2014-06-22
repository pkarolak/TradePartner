@auth.requires_membership('admin')
def index():
    if request.vars.keyword:
        session.keyword = request.vars.keyword
        session.phrase = None
        redirect(URL('search_result'))
    return locals()

def search_result():
    phrase = session.keyword if session.keyword else session.phrase
    session.phrase = phrase
    if (not session.phrase):
        redirect(URL('index'))
    request.vars.keyword = None
    session.keyword = None
    f = db(db.fields.name.contains(phrase, case_sensitive=False)).select(db.fields.id).as_list()
    tmp = []
    for val in f: tmp +=  val.values()
    fields = []
    for val in tmp: fields += str(val)
    grid = SQLFORM.grid(
        (
            db.firms.name.contains(phrase, case_sensitive=False)|
            db.firms.address.contains(phrase, case_sensitive=False)|
            db.firms.city.contains(phrase, case_sensitive=False)|
            db.firms.nip.contains(phrase, case_sensitive=False)|
            db.firms.website.contains(phrase, case_sensitive=False)|
            db.firms.email.contains(phrase, case_sensitive=False)|
            db.firms.phone.contains(phrase, case_sensitive=False)|
            db.firms.categories.contains(fields, all=False) 
        ),
        user_signature=False,
        editable=False,
        deletable=False,
        details=False,
        create=False,
        csv=False,
        links=[
            dict(
                header='',
                body=lambda row: A('Zobacz', _href=URL("firm", "index", args=[row.id]))
            )
        ]
    )
    return locals()

@auth.requires_membership('admin')
def firms():
    grid = SQLFORM.grid(
        db.firms,
        user_signature=False,
        editable=False,
        deletable=False,
        details=False,
        create=False,
        csv=False,
        links=[
            dict(
                header='',
                body=lambda row: A('Wybierz', _href=URL("firm", "index", args=[row.id]))
            ),
        ]

    )
    return locals()

@auth.requires_membership('admin')
def field():
    grid = SQLFORM.grid(
        db.fields,
        user_signature=False,
        editable=True,
        deletable=True,
        details=False,
        create=True,
        csv=False,
    )
    return locals()

@auth.requires_membership('admin')
def users():
    grid = SQLFORM.grid(
        db.auth_user,
        fields = [db.auth_user.id, db.auth_user.first_name, db.auth_user.last_name, db.auth_user.email],
        user_signature=False,
        editable=True,
        deletable=True,
        details=False,
        create=True,
        csv=False,
    )
    return locals()
