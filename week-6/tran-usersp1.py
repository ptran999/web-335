"""
    Title: tran_usersp1.py
    Author: Phuong Tran
    Date: 16/02/2024
    Description: Python MongoDB connection and use.
"""
# import MongoClient
from pymongo import MongoClient

# connect to MongoDB web335DB
client = MongoClient("mongodb+srv://web340_admin:webstudent999@bellevueuniversity.bj68fz9.mongodb.net/?retryWrites=true&w=majority")

# print connection message to the console
print(client)

# establish the database variable
db = client["web335DB"]

# find and display all documents in the collection
for user in db.users.find():
   print(user)

# find a document matching the criteria
print(db.users.find_one({'employeeId': "1011"}))

# find a document matching the criteria
print(db.users.find_one({'lastName': "Mozart"}))