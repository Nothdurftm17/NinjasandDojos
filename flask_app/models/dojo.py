from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja

class Dojo:

    def __init__(self,data):
        self.id = data['id']

        self.name = data['name']

        self.ninjas = []

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#============================================
#Get all Dojos
    @classmethod
    def all_Dojos(cls):
        query = "SELECT * FROM dojos;"
        #connects the sql database
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        print(results)
        #establishes an empty list to for loop the dojo data into
        all_dojos = []
        #for loop that will go through db to find all existing dojos and adds to dojo list page
        for dojos in results:
            all_dojos.append(cls(dojos))
        print(all_dojos)
        return all_dojos

#============================================
#Save creating dojo
    @classmethod
    def save_Dojo(cls, data):
    #query to add dojos 
        query="INSERT INTO dojos(name, created_at) VALUES(%(name)s,NOW());"
        #connects function and query to and back from db
        new_dojo = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return new_dojo
#============================================
# Associating ninja to thier dojo
    @classmethod
    def dojo_get_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db( query , data )
        dojos = cls( results[0] )
        for row_from_db in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"],
                "dojo_id" : row_from_db["dojo_id"]
                
            }
            dojos.ninjas.append( ninja.Ninja(ninja_data))
        return dojos