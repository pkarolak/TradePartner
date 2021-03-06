@auth.requires(auth.has_membership('admin') or auth.has_membership('salesman'))
def new():
	db.transactions.self_representative_id.writable = False
	db.transactions.self_representative_id.default = auth.user.id

	employees = None

#	form = crud.create(db.transactions)

   	form = SQLFORM(db.transactions)
	if form.process().accepted:
		response.flash = 'zapisano transakcję'
		redirect(URL('archive'))
	elif form.errors:
		response.flash = 'znaleziono pewne błędy'
	else:
		response.flash = 'wypełnij formularz'
	return locals()

@auth.requires(auth.has_membership('admin') or auth.has_membership('salesman'))
def archive():
	db.transactions.id.readable = db.transactions.id.writable = False
	if(request.vars["firm_id"]):
		grid = SQLFORM.grid(
	        (db.transactions.firm_id == request.vars["firm_id"]),
	        user_signature=False,
	        editable=False,
	        deletable=False,
	        details=True,
	        create=False,
	        csv=False,
	        searchable=False,
	        maxtextlength=200,
	    	fields = [db.transactions.firm_id, db.transactions.description, db.transactions.self_representative_id],
	    )  
	else:
		grid = SQLFORM.grid(
	        (db.transactions.self_representative_id == auth.user.id),
	        user_signature=False,
	        editable=True,
	        deletable=False,
	        details=True,
	        create=False,
	        csv=False,
	        searchable=False,
	        maxtextlength=200,
	    	fields = [db.transactions.firm_id, db.transactions.description],
	    )
	return locals()


@auth.requires(auth.has_membership('admin'))
def archive_all():
	grid = SQLFORM.grid(
	        db.transactions,
	        user_signature=False,
	        editable=True,
	        deletable=False,
	        details=True,
	        create=False,
	        csv=False,
	        searchable=False,
	        maxtextlength=200,
	    	fields = [db.transactions.firm_id, db.transactions.description, db.transactions.self_representative_id],
	    )
	return locals()

@auth.requires(auth.has_membership('admin') or auth.has_membership('salesman'))
def get_employees():
	if(request.vars["firm_id"]):
		employees = db(db.representatives.firm_id == request.vars["firm_id"])
	return employees
