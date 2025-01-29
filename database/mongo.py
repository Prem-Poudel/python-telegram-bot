from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = 'telegram_bot'

class Mongo:
    def __init__(self):
        try:

            mongo_uri = os.getenv('MONGO_URI')
            if not mongo_uri:
                print('Mongo URI is not set')
                raise ValueError('Mongo URI is not set')
            
            # initialize the client and the database
            self.client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
            self.db = self.client[DB_NAME]

            self.test_connection()

        
        except errors.ServerSelectionTimeoutError as err:
            print(f'Failed to connect to MongoDB: {err}')
            raise
        except Exception as err:
            print(f'An unexpected error occured: {err}')
            raise
     
    def test_connection(self):
        '''Test the connection to the database'''
        try:
            ping_result = self.client.admin.command('ping')
            print(f'Connected to MongoDB. Ping result: {ping_result}')
        except Exception as err:
            print(f'Failed to connect to MongoDB: {err}')
            raise

    
    def get_collection(self, collection_name):
        '''It returns a collection object.'''
        return self.db[collection_name]
    
   
    def close_connection(self):
        '''Close the connection to the database'''
        self.client.close()
        print('Connection to MongoDB closed')


    # user registration
    def register_user(self, first_name, username, chat_id):
        '''Register a user in the database and save the user's information at first interaction.'''
        user_collection = self.get_collection('users')

        if user_collection.find_one({"chat_id": chat_id}):
            return "User already registered."
        
        user_data = {
            "chat_id": chat_id,
            "first_name": first_name,
            "username": username,
        }
        try:
            user_collection.insert_one(user_data)
            return "Registration successful. Please provide your phone number."
        except errors.PyMongoError as err:
            print(f'Failed to register user: {err}')
            return "Failed to register user."
        
    # store user phone number
    def store_phone_number(self, chat_id, phone_number):
        '''Store the user's phone number in the database'''
        user_collection = self.get_collection('users')
        try:
            user_collection.update_one(
            {"chat_id": chat_id},
            {"$set": {"phone_number": phone_number}}
    
        )
            return "Phone number saved successfully."
        except errors.PyMongoError as err:
            print(f'Failed to save phone number: {err}')
            return "Failed to save phone number."