#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask,request,url_for
app=Flask(__name__)

@app.route('/')
def v_index():
	return '''
		<form action="/login" method="POST">
			<input type="text" name="uid" placeholder="输入你的用户ID">
			<input type="password" name="pwd" placeholder="输入你的密码">
			<input type="submit" value="login">
			</form>
	'''

@app.route('/login',methods=['POST'])
def v_login():
	uid= request.form['uid']
	pwd= request.form['pwd']
	if uid=='admin' and pwd=='123':
		return 'Authorized successfully'
	else:
		return 'Un-Authorized'

# app.run(host='0.0.0.0',port=80)
if __name__ == '__main__':
	app.run()




