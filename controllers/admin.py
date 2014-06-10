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
    f = db(db.field.name.contains(phrase, case_sensitive=False)).select(db.field.id).as_list()
    tmp = []
    for val in f: tmp +=  val.values()
    fields = []
    for val in tmp: fields += str(val)
    grid = SQLFORM.grid(
        (
            db.firm.name.contains(phrase, case_sensitive=False)|
            db.firm.address.contains(phrase, case_sensitive=False)|
            db.firm.city.contains(phrase, case_sensitive=False)|
            db.firm.nip.contains(phrase, case_sensitive=False)|
            db.firm.website.contains(phrase, case_sensitive=False)|
            db.firm.email.contains(phrase, case_sensitive=False)|
            db.firm.phone.contains(phrase, case_sensitive=False)|
            db.firm.categories.contains(fields, all=False) 
        ),
        user_signature=False,
        editable=False,
        deletable=False,
        details=False,
        create=False,
        links=[
            dict(
                header='Show',
                body=lambda row: A('Show', _href=URL("firm", "index", args=[row.id]))
            )
        ]
    )
    return locals()

@auth.requires_membership('admin')
def firms():
    grid = SQLFORM.grid(
        db.firm,
        user_signature=False,
        editable=False,
        deletable=False,
        details=False,
        create=False,
        links=[
            dict(
                header='Show',
                body=lambda row: A('Show', _href=URL("firm", "index", args=[row.id]))
            ),
            dict(
                header='Edit',
                body=lambda row: A('Edit', _href=URL("firm", "edit", args=[row.id]))
            )
        ]

    )
    return locals()

@auth.requires_membership('admin')
def category():
    grid = SQLFORM.grid(
        db.category,
        user_signature=False,
        editable=True,
        deletable=True,
        details=False,
        create=True,
    )
    return locals()

@auth.requires_membership('admin')
def field():
    grid = SQLFORM.grid(
        db.field,
        user_signature=False,
        editable=True,
        deletable=True,
        details=False,
        create=True,
    )
    return locals()