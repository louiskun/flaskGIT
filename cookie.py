#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,make_response,url_for
import time

app=Flask(__name__)

def GetNowTime():
	return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

times=GetNowTime()

@app.route('/')
def v_index():
	rsp=make_response('go <a href="%s">page2</a>' % url_for('v_page2'))
	rsp.set_cookie('lastvisit',times)
	return rsp

@app.route('/page2')
def v_page2():
	user=request.cookies['lastvisit']
	return 'time now is %s' % lastvisit

if __name__ == '__main__':
	app.run()

