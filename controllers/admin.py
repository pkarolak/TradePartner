@auth.requires_membership('admin')
def index():
    grid = SQLFORM.grid(
        db.firm,
        user_signature=False,
        editable=True,
        deletable=True,
        details=False,
        create=True,
    )
    return locals()

@auth.requires_membership('admin')
def firms():
    form = FORM(INPUT(_type='button', _value='Add new firm'))
    grid = SQLFORM.grid(
        db.firm,
        user_signature=False,
        editable=False,
        deletable=False,
        details=False,
        create=False,
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