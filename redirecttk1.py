#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask,redirect,request,make_response
app=Flask(__name__)

@app.route('/')
def v_index():
	if request.cookies != None:
		rsp=make_response(redirect('/newbies'))
		rsp.set_cookie('user','tongkun')
		return rsp
	else:
		#如果是新用户，如何处理？
		# rsp=make_response(redirect('/'))	
		# rsp.set_cookie('user','tongkun')	
		# user=request.cookies['user']
		return 'user is news ,you are ?!' 

@app.route('/newbies')
def v_newbies():
	user=request.cookies['user']
	return 'this page is for newbies only!you are %s' % user

if __name__ == '__main__':
	app.run()


