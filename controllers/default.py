# -*- coding: utf-8 -*-
@auth.requires_login()
def index():
	redirect(URL('app', 'index'))

def user():
	return dict(form=auth())
