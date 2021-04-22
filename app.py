from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import json
import math
import os
from flask_mail import Mail, Message
from datetime import datetime

# to open json file
with open("D:/Sandarsh/Flask/code3/templates/config.json",'r') as c:
    param = json.load(c) ["param"]

# if running on local server than local_uri or vice-versa
local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret'
app.config['UPLOAD_FOLDER'] = param['upload_location']
app.config.update(
        MAIL_SERVER = 'smtp.gmail.com',
        MAIL_PORT = '465',
        MAIL_USE_SSL = True,
        MAIL_USERNAME = param['gmail_user'],
        MAIL_PASSWORD = param['gmail_pass']
) #if user sends message in contacts then we will get update through mail
mail = Mail(app) #imported one to take action send mail

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = param['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = param['prod_uri']

db = SQLAlchemy(app)


class Contacts(db.Model):
    s_no = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    phone_no = db.Column(db.Integer, unique = True, nullable = False)
    msg = db.Column(db.String(120), unique = False, nullable = False)
    date = db.Column(db.String(12), unique = False, nullable = True, default = datetime.utcnow)

#making class of both database tables

class Posts(db.Model):
    s_no = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(80), unique = False, nullable = False)
    content = db.Column(db.String(120), unique = False, nullable = False)
    date = db.Column(db.String(12), unique = False, nullable = False, default = datetime.utcnow)
    slug = db.Column(db.String(120), unique = False, nullable = True)
    img_file = db.Column(db.String(12), unique = False, nullable = True)
    tag_line = db.Column(db.String(20), unique = False, nullable = True)

@app.route('/')
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(param['no_of_posts']))
    #[0:param ['no_of_posts']]
    page = request.args.get('page') # int so that we can make calculation
    if(not str(page).isnumeric()):  #if str page is not numeric then make it 0, else is not required as variable is already assigned
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(param['no_of_posts']): (page-1)*int(param['no_of_posts']) + int(param['no_of_posts'])]
    #Pagination logic
    #FIRST PAGE :- start = #, next = page+1
    if (page == 1):
        prev = "#"
        next = "/?page=" + str(page+1)
    elif(page == last):
        prev = "/?page=" + str(page-1)
        next = "#"
    else:
        prev = "/?page=" + str(page-1)
        next = "/?page=" + str(page+1)
    # MIDDLE PAGE :- prev = page-1, next = page+1 // LAST pAGE :- prev = page-1, next = #

    return render_template('index.html', param = param, posts = posts, prev = prev, next = next)

@app.route("/dashboard", methods = ['GET', 'POST'])
def dashboard():
# below first line is for if user is already logged in session
    if ('user' in session and session['user'] == param['admin_user']):
         posts = Posts.query.all()
         return render_template('dashboard.html', param = param, posts = posts)
        #return redirect(request.args.get('dashboard.html'), param=param)

    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == param['admin_user'] and userpass == param['admin_password']):
            #set the session variable
            session['user'] = username
            posts = Posts.query.all()
            #returning page
            return render_template('dashboard.html', param = param, posts = posts)
            #return redirect(request.args.get('dashboard.html'), param=param)
    posts = Posts.query.all()
    return render_template('login.html', param = param, posts = posts)

@app.route("/uploader", methods = ['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == param['admin_user']):
        if request.method == 'POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename) ))
            return "File Uploaded Successfully"

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect("/dashboard")

@app.route("/delete/<string:s_no>", methods = ['GET', 'POST'])
def delete(s_no):
    if ('user' in session and session['user'] == param['admin_user']):
        post = Posts.query.filter_by(s_no = s_no).first()
        db.session.delete(post)
        db.session.commit()
    return redirect("/dashboard")

@app.route("/edit/<string:s_no>", methods = ['GET', 'POST'])
def edit(s_no):
    if ('user' in session and session['user'] == param['admin_user']):   #edit form
        if request.method == 'POST':
            box_title = request.form.get('title')
            content = request.form.get('content')
            slug = request.form.get('slug')
            tag_line = request.form.get('tag_line')
            date = datetime.now()

            if s_no == '0':
                post = Posts(title = box_title, content = content, slug = slug, date = date, tag_line = tag_line, img_file = img_file)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(s_no = s_no).first()
                post.title = box_title
                post.content = content
                post.slug = slug
                post.date = date
                post.tag_line = tag_line
                db.session.commit()
                return redirect('/edit/' + s_no)

        post = Posts.query.filter_by(s_no = s_no).first()

        return render_template('edit.html', param = param, s_no = s_no, post = post)


@app.route('/about')
def about():
    return render_template('about.html', param = param)

@app.route('/booknow')
def book_now():
    return render_template('book.html', param = param)

#for slug
@app.route('/post/<string:post_slug>', methods = ['GET'])
def post_route(post_slug):
    #fetching slug from post from post table slug column
    post = Posts.query.filter_by(slug = post_slug).first()
    #its a rule in flask to pass the string inside def() that has been passed in string
    return render_template('post.html', param = param, post = post)



@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if(request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name = name,date = datetime.now(), phone_no = phone, email = email, msg = message)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from' + name, sender = email, recipients = [param['gmail_user']],
                          body = 'Message : ' + message + "\n" + 'phone no : ' + phone)

    return render_template('contact.html', param = param)

if __name__ == "__main__":
    app.run(debug = True)

#mail.send_message f"New message from  {name}, sender = {email}, recipients = {param['gmail_user']},
                          #body = {message ('\n') phone}"