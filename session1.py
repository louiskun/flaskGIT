#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,session,request
app=Flask(__name__)
app.secret_key='zsdfdgxoo334s'

@app.route('/')
def v_index():
	if 'counter' not in session:
		session['counter'] = 0
	session['counter'] = session['counter'] + 1
	#return '这是你第%d次访问这里' % session['counter']

	return 'session ID: %s' % request.cookies['session']


if __name__ == '__main__':
	app.run()

