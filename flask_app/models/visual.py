
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re

# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt

class Visual:
    db = "visuals" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.genre = data['genre']
        self.approved = data['approved']
        self.NoWhy = data['NoWhy']
        self.notes = data['notes']
        self.rating = data['rating']
        
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        # What changes need to be made above for this project?
        #What needs to be added her for class association?

    @classmethod
    def enter_visual(cls, data):
        if not cls.validate_visual(data):
            return False
        query = """
        INSERT INTO visuals (name, type, genre, approved, NoWhy, notes, rating, user_id)
        VALUES (%(name)s, %(type)s, %(genre)s, %(approved)s, %(NoWhy)s, %(notes)s, %(rating)s, %(user_id)s);
        """
        visual_id = connectToMySQL(cls.db).query_db(query, data)
        return visual_id

    @classmethod
    def get_all_visuals(cls):
        query = """
        SELECT *
        FROM visuals;
        """
        results = connectToMySQL(cls.db).query_db(query)
        all_visuals = []
        for row in results:
            all_visuals.append(cls(row))
        return all_visuals
    
    
    
    @classmethod
    def get_visual_by_id(cls, visual_id):
        query = """
        SELECT * FROM visuals
        WHERE id = %(id)s
        ; """
        results = connectToMySQL(cls.db).query_db(query, {'id':visual_id})
        return cls(results[0])
    
    
    
    @classmethod
    def update(cls, data):
        if not cls.validate_visual(data):
            return False
        query = """
        UPDATE visuals 
        SET name = %(name)s, type = %(type)s, genre = %(genre)s, approved = %(approved)s, NoWhy = %(NoWhy)s, notes = %(notes)s, rating = %(rating)s,updated_at = NOW()
        WHERE id = %(id)s;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return True

    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM visuals
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)
            
    
    @staticmethod
    def validate_visual(data):
        is_valid = True
        if len(data['name']) == 0:
            flash("Name is required")
            is_valid = False
        if len(data['type']) == 0:
            flash("Type is required")
            is_valid = False
        if len(data['genre']) == 0:
            flash("Genre is required")
            is_valid = False
        return is_valid

