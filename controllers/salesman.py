@auth.requires_membership('admin')
def index():
    grid = SQLFORM.grid(
        db.representatives,
        fields = [db.representatives.name, db.representatives.surname, db.representatives.firm_id, db.representatives.email, db.representatives.phone],
        user_signature = False,
        editable = True,
        deletable = True,
        create = True,
        details = False,
        csv = False
    )
    return locals()

