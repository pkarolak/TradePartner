@auth.requires_membership('admin')
def index():
    return locals()

@auth.requires_membership('admin')
def list():
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
