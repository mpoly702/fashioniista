from pymongo import MongoClient
from bson.objectid import ObjectId
from mongoengine import connect, Document, StringField, IntField, ReferenceField, ObjectIdField, DateTimeField
from datetime import datetime
from mongoengine.errors import NotUniqueError
from flask_login import UserMixin
from fashion.login_manager_setup import login_manager


# Establish a connection to the MongoDB database
connect('fashionista', host='mongodb://localhost:27017/')

# Define the User model
class User(UserMixin, Document):
    meta = {'collection': 'users'}

    fullname = StringField(max_length=64, required=True)
    email = StringField(max_length=64, unique=True, required=True)
    password_hash = StringField(max_length=128)
    phone_number = StringField(required=True)


# Use the User model to interact with the users collection
def create_user(user_data):
    existing_user = User.objects(fullname=user_data.get('fullname')).first()
    if existing_user:
        raise NotUniqueError(f"A user with fullname '{user_data['fullname']}' already exists.")
    user = User(**user_data)
    user.save()
    return {
    "message": f"User {user.fullname} created successfully",
    "user_id": user.id
}

def get_user(email):
    return User.objects(email=email).first()



# Blog Model
class BlogPost(Document):
    meta = {'collection': 'blogs'}

    title = StringField(max_length=120, required=True)
    content = StringField(required=True)
    author = ReferenceField('User', required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)




