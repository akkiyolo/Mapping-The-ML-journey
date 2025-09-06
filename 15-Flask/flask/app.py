from flask import Flask
'''
It creates an instance of the flask class,
which will be your WSGI(web server gateway interface) application
'''
### WSGI application

app=Flask(__name__)

@app.route("/") ## okay so when the particular route that is / which is for home page is being hit we will be redirected to the home page
def welcome():
  return "welcome to this flask app.This should be an amazing course.New changes made, what else could you learn when you got python"

@app.route("/index")
def hey():
  return "index is a new route or endpoint of the url"

if __name__=="__main__":
  app.run(debug=True) # this command automatically starts the server
