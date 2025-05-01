# from mongo_api_client.MongoApiClient import MongoApiClient, MongoApiReponse
# from typing import Any, Dict, List


# server = MongoApiClient("localhost", 9777, "", "http")

# data : MongoApiReponse  = (
#     server
#     .use_db("isac-division2-api")
#     .use_collection("stats_versioning")
#     .where("identifier", "=", "22edd328-96ff-4831-bc73-723e91b5f29d")
#     .group_by("stats.burningKills")
#     .sort_by("_id", "desc")
#     .all()
# )

# print(data.get_data())

# # query: List[Dict[str, Any]] = [
# #     {"$match": {"stats.timePlayed": {"$gte": 10000}}},
# # ]


# # data : MongoApiReponse  = (
# #     server
# #     .use_db("isac-division2-api")
# #     .use_collection("stats_versioning")
# #     .per_page(2)
# #     .execute_custom_query(query, True)
# # )

# # print(data.get_data())

# # print(data.get_data())

# # dbs = server.list_databases()

# # print(dbs.get_databases())

# # delete = server.delete_database("test")

# # print(delete.get_error())



# # print(
# #     database.from_db("isac_v2_logging").from_table("bot_logs").sort_by('_id', 'desc').per_page(20).page(1).find()
# # )
# # print(database
# #  .from_db("isac-division2-bot")
# #  .from_table("account-versioning")
# #  .per_page(2)
# #  .page(1)
# #  .sort_by("created_at","desc")
# #  .select())

# # print(database.list_tables_in_db("isac-division2-bot"))

# # testData = [
# #     {
# #     'username' : 'hoewea2342we',
# #     'age' : 21,
# #     'ocupations' : ['software engineer', 'musician']
# # },
# #     {
# #     'username' : 'hoeweaasdeasdwe',
# #     'age' : 44,
# #     'ocupations' : ['software engineer', 'musician']
# # },
# #     {
# #     'username' : 'hoewea111we',
# #     'age' : 23,
# #     'ocupations' : ['software engineer', 'musician']
# # }
# # ]

# # print(database.into_db('my-test-database').into_table('my-test-table-2').insert(testData))
# # print(
# #     database.from_db("my-test-database")
# #     .from_table("my-test-table")
# #     .delete_by_id("665104538e80ecc6f646d6cd")
# # )

# # print(database.delete_database("alexanderdth"))

# # print(database.delete_tables_in_db("my-test-database", "my-test-table-2"))

# # print(
# #     database
# #     .from_db("my-test-database")
# #     .from_table("my-test-table")
# #     .or_where("username", "=", "hoeweaasdeasdwe")
# #     .or_where("age", "=", 21)
# #     .delete()
# # )

# # print(
# #     database
# #     .into_db("my-test-database")
# #     .into_table("my-test-table")
# #     .where("username", "=", "hoewea111we")
# #     .update({
# #         "username": "alexanderdth123",
# #         "age": 99
# #     })
# # )

# # print(
# #     database
# #     .from_db("my-test-database")
# #     .from_table("my-test-table")
# #     .update_by_id("665103498e80ecc6f646d6c5", {
# #         "username" : "popeye1212"
# #     })
# # )

# # print(database.from_db('my-test-database').from_table('my-test-table').get().first())
# # print(database
# #       .from_db('isac-division2-bot')
# #       .from_table('account-versioning')
# #       .where('identifier', '=', '7e14ad6b-0264-4d2a-ab78-e57f008d9da1')
# #       .sort_by('created_at','desc')
# #       .get()
# #       .first())

# # print(database
# #       .from_db('isac-division2-bot')
# #       .from_table('account-versioning')
# #       .count())
