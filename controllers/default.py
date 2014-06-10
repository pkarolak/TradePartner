# -*- coding: utf-8 -*-
@auth.requires_login()
def index():
	redirect(URL('admin', 'index'))

def user():
	return dict(form=auth())
