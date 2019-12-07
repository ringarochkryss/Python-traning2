import os

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
mongo_uri = os.environ.get('MONGO_URI')

print(db_user)
print(db_password)