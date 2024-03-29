from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    data = {"name":"pinzaa","age":"30","salary":"100000"}
    return render_template("index.html",mydata = data)

@app.route('/about')
def about():
    products = ["เสื้อผ้า","เตารีด","ผ้าห่ม","ยาสามัญ"]
    return render_template("about.html",myproducts = products)

@app.route('/admin')
def profile():
    username = "pin"
    return render_template("admin.html", username = username)

@app.route('/user/<name>/<age>')
def member(name,age):
    return "ชื่อ : {} , อายุ : {} ".format(name,age)

@app.route('/sendData')
def signupForm():
    fname = request.args.get('fname')
    description = request.args.get('description')
    return render_template("thankyou.html",data={"name":fname,"description":description})


if __name__ == "__main__":
    app.run(debug=True)

