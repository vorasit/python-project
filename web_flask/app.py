from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return " <h1>Hello World </h1>"

@app.route('/about')
def about():
    return "<h1> เกี่ยวกับฉัน </h1>"

@app.route('/admin')
def profile():
    return "<h1> สวัสดีครับ Admin  </h1>"

@app.route('/user/<name>/<age>')
def member(name,age):
    return "ชื่อ : {} , อายุ : {} ".format(name,age)




if __name__ == "__main__":
    app.run(debug=True)

