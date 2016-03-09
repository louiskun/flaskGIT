#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask,redirect
app=Flask(__name__)

@app.route('/')
def v_index():
	return redirect('/newbies')

@app.route('/newbies')
	return 'this page is for newbies only!'

if __name__ == '__main__':
	app.run()


