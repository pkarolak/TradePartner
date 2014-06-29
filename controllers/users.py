@auth.requires_membership('admin')
def index():
    return locals()

@auth.requires_membership('admin')
def list():

    gridNA = SQLFORM.grid(
        db.auth_user.registration_key == 'pending',
        user_signature=False,
        editable=False,
        deletable=False,
        details=False,
        create=False,
        searchable=False,
        links=[dict(
            header='Aktywacja',
            body=lambda row: A('aktywuj', _href=URL("activate", args=[row.id]))
        )],
        csv=False,
    )

    grid = SQLFORM.grid(
        db.auth_user,
        fields = [db.auth_user.id, db.auth_user.first_name, db.auth_user.last_name, db.auth_user.email],
        user_signature = False,
        editable = True,
        deletable = True,
        details = False,
        create = True,
        csv = False
    )

    return locals()


@auth.requires_membership('admin')
def activate():
    if request.args(0) != '':
        db(db.auth_user.id == request.args(0)).update(registration_key='')
    session.flash = 'Konto zostało aktywowane.'
    redirect(URL('list'))