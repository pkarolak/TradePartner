# -*- coding: utf-8 -*-
@auth.requires_login()
def index():
	if auth.has_membership("admin"):
		redirect(URL('admin', 'index'))
   	return dict('błąd')

def user():
	return dict(form=auth())
