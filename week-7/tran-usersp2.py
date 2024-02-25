"""
    Title: tran-usersp2.py
    Author: Phuong Tran
    Date: 02/23/2024
    Description: Python with MongoDB.
"""
# import MongoClient
from pymongo import MongoClient
import datetime

# connect to MongoDB web335DB
client = MongoClient("mongodb+srv://web340_admin:webstudent999@bellevueuniversity.bj68fz9.mongodb.net/?retryWrites=true&w=majority")

# print connection message to the console
print(client)

# establish the database variable
db = client["web335DB"]

# create a new document in the users collection
db.users.insert_one({
  "firstName": "Phuong",
  "lastName": "Test",
  "employeeId": "1900",
  "email": "ptest@me.com",
  "dateCreated": datetime.datetime.now()
})

# query and print the collection for the updated document
print(db.users.find_one({
  "firstName": "Phuong",
  "lastName": "Test"
}))

# update the email for the new document
db.users.update_one(
  {"firstName": "Phuong", "lastName": "Test"},
  {"$set": {"email": "phuongtest@me.com"}}
)

# query and print the collection for the updated document
print(db.users.find_one({
  "firstName": "Phuong",
  "lastName": "Test"
}))

# delete a specific document
db.users.delete_one({
  "firstName": "Phuong",
  "lastName": "Test"
})

# query the collection for a specific document
print(db.users.find_one({
  "firstName": "Phuong",
  "lastName": "Test"
}))