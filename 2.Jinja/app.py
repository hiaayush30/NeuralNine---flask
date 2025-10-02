from flask import Flask,render_template,redirect,url_for

app = Flask(__name__,template_folder='templates')

@app.route("/")
def hello():
    value = "Aayush"
    li = [10,20,30]
    return render_template('index.html',name=value, list=li)

@app.route("/filters2")
def filtersPage():
    return render_template("filters.html",some_text="random text argument")

# creating a custom filter for jinja
@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat_string')
def repeat(s,times):
    return s*times

@app.template_filter("alternate_case")
def alternate_case(s):
    return "".join([c.upper() if i%2==0 else c.lower() for i,c in enumerate(s)])

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('filtersPage'))

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)