from flask import Flask
'''
It creates an instance of the flask class,
which will be your WSGI(web server gateway interface) application
'''
### WSGI application

app=Flask(__name__)


if __name__=="__main__":
  app.run()
