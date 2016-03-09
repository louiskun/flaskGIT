#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,abort,request
app=Flask(__name__)

@app.route('/')
def v_index():
	return '''
		<ul>
		    <li><a href="/admin?token=78787878">允许访问</a></li>
		    <li><a href="/admin">请求被禁止</a></li>
		</ul>
	'''

@app.route('/admin')
def v_admin():
	if request.args['token'] == '78787878':
		return 'you are a good boy!'
	else:
		abort(401)

if __name__ == '__main__':
	app.run()

