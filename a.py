from pprint import pprint

from database import Database
db = Database()
for row in db.fetch_movies():
    print(row)
