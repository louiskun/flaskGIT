#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask,json,make_response
app=Flask(__name__)

users=['Linda','Marion5','Race8']

@app.route('/')
def v_index():
	#response对象返回：
    rsp=make_response(json.dumps(users))
    rsp.mimetype='application/json'
    rsp.charset='utf-8'
    rsp.status_code=200
    rsp.headers['x-tag']='str,magic'
    return rsp
	
	#直接返回：
	# return json.dumps(users),200,[('Content-type','application/json;charset=utf-8')]

if __name__ == '__main__':
	app.run()

