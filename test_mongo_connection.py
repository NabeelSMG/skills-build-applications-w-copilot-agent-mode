from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Test inserting data into the 'users' collection
def test_insert():
    try:
        db.users.insert_one({"username": "testuser", "email": "testuser@example.com", "password": "password123"})
        print("Data inserted successfully into 'users' collection.")
    except Exception as e:
        print(f"Error inserting data: {e}")

# Test retrieving data from the 'users' collection
def test_retrieve():
    try:
        users = list(db.users.find())
        print("Retrieved users:", users)
    except Exception as e:
        print(f"Error retrieving data: {e}")

if __name__ == "__main__":
    test_insert()
    test_retrieve()
