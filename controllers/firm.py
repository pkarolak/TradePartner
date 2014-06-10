def index():
	crud.settings.formstyle = 'divs'
	firm = db.firm(request.args(0,cast=int)) or redirect(URL('index'))
	form = crud.read(db.firm, firm)
		

	"""
	db.post.page_id.default = this_page.id
	form = SQLFORM(db.post).process() if auth.user else None
	pagecomments = db(db.post.page_id==this_page.id).select()
	"""
	return locals()

def new():
	crud.settings.formstyle = 'divs'
	form = crud.create(db.firm)
	if form.process().accepted:
		response.flash = 'form accepted'
	elif form.errors:
		response.flash = 'form has errors'
	else:
		response.flash = 'please fill out the form'
	return locals()

def edit():
	crud.settings.formstyle = 'divs'
	if request.args(0):
		firm_id = request.args(0)
	form = crud.update(db.firm, firm_id)
	if form.process().accepted:
		response.flash = 'form accepted'
	elif form.errors:
		response.flash = 'form has errors'
	else:
		response.flash = 'please fill out the form'
	return locals()

def delete():
	return locals()

