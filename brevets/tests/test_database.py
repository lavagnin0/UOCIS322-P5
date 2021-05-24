"""
Nosetests for the database.
The following functionality is required for the application and will be tested:
- Checking if the database is empty
- Inserting sets of times one at a time
- Checking if a distance is already in the database
- Retrieving everything from the database
- Deleting everything from the database
"""
import nose
from pymongo import MongoClient
import os

###
# Globals
###
client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.testdb


def test_all_database_functionality():
    #test checking emptiness of database with count_documents, should start empty
    assert db.testdb.count_documents({}) == 0

    #test insertion of example entry, should be able to find it using just dist value
    example_entry = {
            'dist': 0,
            'open': '2021-01-01T00:00',
            'close': '2021-01-01T01:00',
        }
    db.testdb.insert_one(example_entry)
    assert db.testdb.find_one({"dist": 0}) == example_entry
    assert db.testdb.count_documents({}) == 1

    #test another entry can be inserted and checked for
    example_entry2 = {
        'dist': 100,
        'open': '2021-01-01T04:00',
        'close': '2021-01-01T10:00',
    }
    db.testdb.insert_one(example_entry2)
    assert db.testdb.find_one({"dist": 100}) == example_entry2
    assert db.testdb.count_documents({}) == 2

    #test extraction of all entries
    items = list(db.testdb.find())
    assert len(items) == 2

    #test deletion of all entries
    db.testdb.delete_many({})
    assert db.testdb.find_one({"dist": 0}) is None
    assert db.testdb.find_one({"dist": 100}) is None
    assert db.testdb.count_documents({}) == 0
