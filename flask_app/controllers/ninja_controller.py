
from flask_app import app
from flask import render_template,request, redirect
# import the class from friend.py
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

#======================================================
# route to render add ninja
@app.route('/create_Ninja')
def create_Ninja():
    all_Dojos = Dojo.all_Dojos()
    return render_template("create_Ninja.html", dojos = all_Dojos)

#======================================================
# route that processes the post
@app.route('/creating_Ninja', methods=['POST'])
def creating_Ninja():
    data ={
        "dojo_id" : request.form['dojo_id'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age']
    }

    Ninja.save_ninja(data)
    return redirect("/")
#======================================================
