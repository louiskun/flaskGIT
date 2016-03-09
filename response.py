#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,make_response,url_for
app=Flask(__name__)

@app.route('/')
def v_index():
	return '<a href="%s">ping</a>' % url_for('v_ping')

@app.route('/ping')
def v_ping():
	return 'pong',200,{'x-tag':'sth.magic'}
	
if __name__ == '__main__':
	app.run()

