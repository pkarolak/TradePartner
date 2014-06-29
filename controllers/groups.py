@auth.requires_membership('admin')
def index():
    grid = SQLFORM.grid(
        db.auth_membership,
        fields = [db.auth_membership.id, db.auth_membership.user_id, db.auth_membership.group_id],
        user_signature = False,
        editable = True,
        deletable = True,
        details = False,
        create = True,
        csv = False
    )
    return locals()

@auth.requires_membership('admin')
def list():
    grid = SQLFORM.grid(
        db.auth_group,
        fields = [db.auth_group.role, db.auth_group.description],
        user_signature = False,
        editable = True,
        deletable = True,
        details = False,
        create = True,
        csv = False
    )
    return locals()

@auth.requires_membership('admin')
def new():
    form = crud.create(db.auth_group)
    if form.process().accepted:
        response.flash = 'Dodano nową grupę'
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'Nie udało się dodać grupy'
    else:
        response.flash = 'Wypełnij formularz'


    return locals()

