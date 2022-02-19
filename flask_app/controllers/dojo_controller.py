
from flask_app import app
from flask import render_template,request, redirect
# import the class from dojo.py
from flask_app.models.dojo import Dojo

#===========================================================
@app.route("/")
def index():
#other code to be added

#list all dojos
    all_dojos = Dojo.all_Dojos()
    return render_template("index.html", all_dojos = all_dojos)

#===========================================================

#===========================================================
# route processing the creation of new_dojo

@app.route("/creatingDojo", methods=['POST'])
def creatingDojo():
    #this is where your request.form data is entered
    data = {
        "name" : request.form['name']
    }
    #class.(name of saving new add function)
    Dojo.save_Dojo(data)
    return redirect("/")
#===========================================================

#===========================================================
#add route that renders to Dojo_members
@app.route("/<int:dojo_id>")
def Dojo_members(dojo_id):
    data={

        "id" : dojo_id
    }
    dojos = Dojo.dojo_get_ninjas(data)
    return render_template("Dojo_members.html", dojo = dojos)
#===========================================================