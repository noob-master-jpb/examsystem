from app import *


@app.route("/",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form['uname']
        psw = request.form['psw']
        with app.app_context():
            auth = Login(get_db())
            print(auth.login_data_user(user,what = 'password'))
            print(psw)
            if psw == auth.login_data_user(user,what = 'password')[0][0]:
                if user in auth.admin_list():
                    return redirect(url_for("admin"))
                return redirect(url_for("student",userid = user))
    return render_template("login.html")
