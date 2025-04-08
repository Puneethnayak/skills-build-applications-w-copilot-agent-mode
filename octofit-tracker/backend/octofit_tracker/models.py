from pymongo import MongoClient

# Replace djongo models with pymongo client for MongoDB integration
client = MongoClient('localhost', 27017)
db = client['octofit_db']
