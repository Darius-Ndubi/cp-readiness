from flask import Flask


#initialize the app
app=Flask(__name__)

#set app secret key
app.secret_key = '\xaa\x98\xfb\xf7\xcb?\xce\xd3\xdf\x96'

#load the views
from app import views

#load the config file
app.config.from_object('config')
