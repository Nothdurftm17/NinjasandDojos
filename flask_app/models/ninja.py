from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.dojo_id = data['dojo_id']

# ==================================================
# class method for saving the added ninja
    @classmethod
    def save_ninja(cls, data):
        
        query = "INSERT INTO ninjas(first_name, last_name, age, created_at, dojo_id) VALUES(%(first_name)s,%(last_name)s,%(age)s, NOW(),%(dojo_id)s);"
        new_ninja = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return new_ninja
# ==================================================