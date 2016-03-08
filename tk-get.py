#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,url_for
app=Flask(__name__)

@app.route('/')
def v_index():
	return '''
		<form method='GET' action='/search'>
			<input type='text' placeholder='输入关键字' value='Python Flask' name='q'>
			<input type='submit' value='search'>
		</form>
	'''

@app.route('/search')
def v_search():
	if 'q' in request.args:
		ret='<p>searching %s...</p>' % request.args['q']
	else:
		ret='what do you want to search?'
	return ret

if __name__ == '__main__':
	app.run()

