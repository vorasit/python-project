from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {"name":"pinzaa","age":"30","salary":"100000"}
    return render_template("index.html",mydata = data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/admin')
def profile():
    name = "pinzaa"
    age = 26
    return render_template("admin.html",myname = name, myage = age)

@app.route('/user/<name>/<age>')
def member(name,age):
    return "ชื่อ : {} , อายุ : {} ".format(name,age)




if __name__ == "__main__":
    app.run(debug=True)

