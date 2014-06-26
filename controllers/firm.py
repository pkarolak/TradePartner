def index():

	firm = db.firms(request.vars["firm_id"]) or redirect(URL('index'))
	form = crud.read(db.firms, firm)
	rate = db.firms(request.vars["firm_id"]).rating	
	if( db((db.likes.firm_id == request.vars["firm_id"])).count() == 0):
		likable = True
	else:
		likable = False
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
		response.flash = 'form accepted'
	elif form.errors:
		response.flash = 'form has errors'
	else:
		response.flash = 'please fill out the form'
	return locals()

@auth.requires_membership('admin')
def edit():
	if request.vars["firm_id"]:
		firm_id = request.vars["firm_id"]
	form = crud.update(db.firms, firm_id)
	if form.process().accepted:
		response.flash = 'form accepted'
	elif form.errors:
		response.flash = 'form has errors'
	else:
		response.flash = 'please fill out the form'
	return locals()

@auth.requires_membership('admin')
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

def delete():
	return locals()

