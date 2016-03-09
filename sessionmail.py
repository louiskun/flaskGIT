# -*- coding:utf-8 -*-
from flask import Flask,request,session,redirect,url_for

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    
@app.route('/')
def v_inbox():	
    #if 'username' in session:
    #    return '<h1>%s\' mailbox</h1>' % session['username']       
    #else:
	return 'not authorized.go <a href="%s">here</a> to authorize yourself' % url_for('v_auth')

@app.route('/login',methods=["POST","GET"])
def v_auth():
    if request.method == 'GET':
        return  '''
                <form action="%s" method="POST">
                    <input type="text" name="username" placeholder="input your username">
                    <input type="password" name="password" placeholder="input your password">
                    <input type="submit" value="submit">
                </form>
                ''' % url_for('v_auth')
    if request.method == 'POST':
        if request.form['username'] == 'jason' and request.form['password'] == '7878':
        	session['username'] = request.form['username']
        return "<h1>%s mailbox</h1>" % session['username']
          
        
            #return  'authorized! go <a href="%s">inbox</a>' % url_for('v_inbox') 
if __name__ == '__main__':
	app.run()
	



