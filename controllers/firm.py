@auth.requires(auth.has_membership('admin') or auth.has_membership('salesman'))
def index():
	firm = db.firms(request.vars["firm_id"]) or redirect(URL('admin','firms'))
	form = crud.read(db.firms, firm)
	rate = db.firms(request.vars["firm_id"]).rating	
	if( db((db.likes.firm_id == request.vars["firm_id"])).count() == 0):
		likable = True
	else:
		likable = False

	db.comments.firm_id.default = request.vars["firm_id"]	
	db.comments.firm_id.readable = False	
	db.comments.firm_id.writable = False

	db.comments.self_representative_id.default = auth.user.id	
	db.comments.self_representative_id.readable = False	
	db.comments.self_representative_id.writable = False

	add = crud.create(db.comments,)
	if add.process().accepted:
		response.flash = 'zapisano transakcję'
		redirect(URL("index", vars={"firm_id":request.vars["firm_id"]}))
	elif add.errors:
		response.flash = 'znaleziono pewne błędy'
	comments = db(db.comments.firm_id == request.vars["firm_id"]).select()

	"""
	db.post.page_id.default = this_page.id
	form = SQLFORM(db.post).process() if auth.user else None
	pagecomments = db(db.post.page_id==this_page.id).select()
	"""
	return locals()

@auth.requires_membership('admin')
def new():
	form = crud.create(db.firms)
	if form.process().accepted:
		response.flash = 'zapisano transakcję'
	elif form.errors:
		response.flash = 'znaleziono pewne błędy'
	else:
		response.flash = 'wypełnij formularz'
	return locals()

@auth.requires_membership('admin')
def edit():
	if request.vars["firm_id"]:
		firm_id = request.vars["firm_id"]
	form = crud.update(db.firms, firm_id)
	if form.process().accepted:
		response.flash = 'zapisano transakcję'
	elif form.errors:
		response.flash = 'znaleziono pewne błędy'
	else:
		response.flash = 'wypełnij formularz'
	return locals()

@auth.requires(has_membership('admin') or has_membership('salesman'))
def representatives():
	 grid = SQLFORM.grid(
        (db.representatives.firm_id == request.vars["firm_id"]),
        user_signature=False,
        editable=True,
        deletable=False,
        details=True,
        create=True,
        csv=False,
        fields=[db.representatives.name,db.representatives.surname,db.representatives.email,db.representatives.phone,],
        maxtextlength=200,
        )
	 return locals()

@auth.requires_membership('admin')
def like():
	db(db.firms.id == request.vars["firm_id"]).update(rating = db.firms(request.vars["firm_id"]).rating + 1)
	db.likes.insert(firm_id=request.vars["firm_id"], liker=auth.user.id)
	redirect(URL("index", vars={"firm_id":request.vars["firm_id"]}))
	return 'done'


@auth.requires_membership('admin')
def dislike():
	db(db.firms.id == request.vars["firm_id"]).update(rating = db.firms(request.vars["firm_id"]).rating - 1)
	db((db.likes.firm_id==request.vars["firm_id"]) & (db.likes.liker==auth.user.id)).delete()
	redirect(URL("index", vars={"firm_id":request.vars["firm_id"]}))
	return 'done'

@auth.requires_membership('admin')
def add_comment():
	db.comments.insert(firm_id=request.vars["firm_id"], self_representative_id=auth.user.id, comment=request.vars["comment"], outer_representative_id=request.vars["outer_representative_id"])	
	redirect(URL("index", vars={"firm_id":request.vars["firm_id"]}))
	return 'done'

@auth.requires_membership('admin')
def delete():
	return locals()
