@auth.requires(auth.has_membership('admin') or auth.has_membership('salesman'))
def index():
    if request.vars.keyword:
        session.keyword = request.vars.keyword
        session.phrase = None
        redirect(URL('search_result'))
    return locals()

@auth.requires(auth.has_membership('admin') or auth.has_membership('salesman'))
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
                body=lambda row: A('Zobacz', _href=URL("firm", "index", vars={"firm_id":[row.id]}))
            )
        ],
        orderby = ~db.firms.rating,
    )
    return locals()

@auth.requires(auth.has_membership('admin') or auth.has_membership('salesman'))
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
                body=lambda row: A('Wybierz', _href=URL("firm", "index", vars={"firm_id":[row.id]}))
            ),
        ],
        orderby = ~db.firms.rating,

    )
    return locals()

@auth.requires(auth.has_membership('admin') or auth.has_membership('salesman'))
def field():
    grid = SQLFORM.grid(
        db.fields,
        user_signature=False,
        editable=False,
        deletable=True,
        details=False,
        create=True,
        csv=False,
        fields = [db.fields.name,]
    )
    return locals()

