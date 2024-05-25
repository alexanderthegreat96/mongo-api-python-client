from MongoApiClient import MongoApiClient

database = MongoApiClient("192.168.1.69", 9875, "http")

# print(database
#  .from_db("isac-division2-bot")
#  .from_table("account-versioning")
#  .per_page(2)
#  .page(1)
#  .sort_by("created_at","desc")
#  .select())

# print(database.list_tables_in_db("isac-division2-bot"))

# testData = [
#     {
#     'username' : 'hoewea2342we',
#     'age' : 21,
#     'ocupations' : ['software engineer', 'musician']
# },
#     {
#     'username' : 'hoeweaasdeasdwe',
#     'age' : 44,
#     'ocupations' : ['software engineer', 'musician']
# },
#     {
#     'username' : 'hoewea111we',
#     'age' : 23,
#     'ocupations' : ['software engineer', 'musician']
# }
# ]

# print(database.into_db('my-test-database').into_table('my-test-table-2').insert(testData))
# print(
#     database.from_db("my-test-database")
#     .from_table("my-test-table")
#     .delete_by_id("665104538e80ecc6f646d6cd")
# )

# print(database.delete_database("alexanderdth"))

# print(database.delete_tables_in_db("my-test-database", "my-test-table-2"))

# print(
#     database
#     .from_db("my-test-database")
#     .from_table("my-test-table")
#     .or_where("username", "=", "hoeweaasdeasdwe")
#     .or_where("age", "=", 21)
#     .delete()
# )

# print(
#     database
#     .into_db("my-test-database")
#     .into_table("my-test-table")
#     .where("username", "=", "hoewea111we")
#     .update({
#         "username": "alexanderdth123",
#         "age": 99
#     })
# )

# print(
#     database
#     .from_db("my-test-database")
#     .from_table("my-test-table")
#     .update_by_id("665103498e80ecc6f646d6c5", {
#         "username" : "popeye1212"
#     })
# )
