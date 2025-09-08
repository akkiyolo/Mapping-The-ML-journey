## building url dynamically
## Variable rule
## jinja 2 template engine

## jinja 2 template engine 
'''
{{}} expressions to print output in html
{%...%} condition, for loops
{#...#} this is for comments
'''

from flask import Flask,render_template,request

app=Flask(__name__)


@app.route("/") 
def welcome():
  return render_template('home.html')

@app.route("/index",methods=['GET'])
def hey():
  return render_template('index.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/submit",methods=['GET','POST'])
def form():
  if request.method=='POST':
    name=request.form['name']
    return f"Hello {name}"
  return render_template('form.html')


##variable rule : we are asking to return a specific value 
@app.route("/successres/<int:score>")
def successres(score):
  res=""
  if score>=50:
    return "PASSED"
  else:
    return "FAILED"
  
  exp={'score':score,"res":res}
  
  return render_template('result1.html',results=exp)

if __name__=="__main__":
  app.run(debug=True) # this command automatically starts the server
