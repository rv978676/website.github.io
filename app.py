from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    #return render_templete('from_index.html')
    return '<h1>hello</h1>'

@app.route('/<name>')
def hello(name):
    return '<h1>hello {}</h1>'.format(name)