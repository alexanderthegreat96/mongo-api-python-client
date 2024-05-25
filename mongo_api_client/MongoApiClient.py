import requests
import json
from typing import Union


class MongoApiClient:
    """
        Just the basic constructor containing various data 
        contained across the application
    """
    def __init__(
        self, server_url: str = None, server_port: int = 0, scheme: str = "http"
    ) -> None:
        self.__server_url = server_url
        self.__server_port = server_port
        self.__api_url = scheme + "://" + server_url + ":" + str(server_port)

        self.__db_name = None
        self.__table_name = None
        self.__per_page = 0
        self.__page = 0

        self.__query_params = {}

        self.__where_query = []
        self.__or_where_query = []
        self.__sort_by_list = []

        self.__operator_map = {
            "=": "=",
            "!=": "!=",
            "<": "<",
            "<=": "<=",
            ">": ">",
            ">=": ">=",
            "like": "_like_",
        }

        self.__sort_order = ["asc", "desc"]

    def __assemble_query(self):
        if len(self.__where_query) > 0:
            self.__query_params["query_and"] = "[" + "|".join(self.__where_query) + "]"

        if len(self.__or_where_query) > 0:
            self.__query_params["query_or"] = (
                "[" + "|".join(self.__or_where_query) + "]"
            )

        if self.__per_page > 0:
            self.__query_params["per_page"] = self.__per_page

        if self.__page > 0:
            self.__query_params["page"] = self.__page

        if len(self.__sort_by_list) > 0:
            self.__query_params["sort"] = "[" + "|".join(self.__sort_by_list) + "]"

    def __make_select_request(self) -> dict:
        request_url = (
            self.__api_url
            + "/db/"
            + self.__db_name
            + "/"
            + self.__table_name
            + "/select"
        )
        headers = {"accept": "application/json"}
        try:
            response = requests.get(
                request_url, params=self.__query_params, headers=headers, timeout=5
            )
            return response.json()
        except Exception as e:
            return {
                "status": False,
                "error": "Unable to retrieve data. Error:" + str(e),
            }

    def __make_insert_request(self, data: Union[dict, list] = None) -> dict:
        if not data:
            return {
                "status": False,
                "error": "You failed to provide some data to send to the server",
            }
        request_url = (
            self.__api_url
            + "/db/"
            + self.__db_name
            + "/"
            + self.__table_name
            + "/insert"
        )
        payload = {"payload": json.dumps(data)}

        try:
            response = requests.post(
                request_url,
                data=payload,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=5,
            )

            return response.json()
        except Exception as e:
            return {
                "status": False,
                "error": "Unable to insert data: " + str(e),
            }

    def __make_insert_if_request(self, data: Union[dict, list] = None) -> dict:
        if not data:
            return {
                "status": False,
                "error": "You failed to provide some data to send to the server",
            }
        request_url = (
            self.__api_url
            + "/db/"
            + self.__db_name
            + "/"
            + self.__table_name
            + "/insert-if"
        )
        payload = {"payload": json.dumps(data)}

        try:
            response = requests.post(
                request_url,
                data=payload,
                params=self.__query_params,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=5,
            )

            return response.json()
        except Exception as e:
            return {
                "status": False,
                "error": "Unable to insert data: " + str(e),
            }

    def __make_select_by_id_request(self, mongo_id: str = None) -> dict:
        if not mongo_id:
            return {
                "status": False,
                "error": "You failed to provide a Mongo record ID.",
            }
        request_url = (
            self.__api_url
            + "/db/"
            + self.__db_name
            + "/"
            + self.__table_name
            + "/get/"
            + mongo_id
        )
        headers = {"accept": "application/json"}
        try:
            response = requests.get(request_url, headers=headers, timeout=5)
            return response.json()
        except Exception as e:
            return {
                "status": False,
                "error": "Unable to retrieve data. Error:" + str(e),
            }

    def __make_delete_by_id_request(self, mongo_id: str = None) -> dict:
        if not mongo_id:
            return {
                "status": False,
                "error": "You failed to provide a Mongo record ID.",
            }
        request_url = (
            self.__api_url
            + "/db/"
            + self.__db_name
            + "/"
            + self.__table_name
            + "/delete/"
            + mongo_id
        )
        headers = {"accept": "application/json"}
        try:
            response = requests.delete(request_url, headers=headers, timeout=5)
            return response.json()
        except Exception as e:
            return {
                "status": False,
                "error": "Unable to delete data. Error:" + str(e),
            }

    def __make_update_request(self, data: Union[dict, list] = None) -> dict:
        if not data:
            return {
                "status": False,
                "error": "You failed to provide some data to send to the server",
            }
        request_url = (
            self.__api_url
            + "/db/"
            + self.__db_name
            + "/"
            + self.__table_name
            + "/update-where"
        )
        payload = {"payload": json.dumps(data)}

        try:
            response = requests.put(
                request_url,
                data=payload,
                params=self.__query_params,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=5,
            )

            return response.json()
        except Exception as e:
            return {
                "status": False,
                "error": "Unable to update data: " + str(e),
            }

    def __make_update_request_by_id(
        self, mongo_id: str = None, data: Union[dict, list] = None
    ) -> dict:
        if not data and not mongo_id:
            return {
                "status": False,
                "error": "You failed to provide some data + mongo_id to send to the server",
            }
        request_url = (
            self.__api_url
            + "/db/"
            + self.__db_name
            + "/"
            + self.__table_name
            + "/update/"
            + mongo_id
        )
        payload = {"payload": json.dumps(data)}

        try:
            response = requests.put(
                request_url,
                data=payload,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=5,
            )

            return response.json()
        except Exception as e:
            return {
                "status": False,
                "error": "Unable to update data: " + str(e),
            }

    def __make_delete_request(self) -> dict:
        request_url = (
            self.__api_url
            + "/db/"
            + self.__db_name
            + "/"
            + self.__table_name
            + "/delete-where"
        )
        headers = {"accept": "application/json"}
        try:
            response = requests.delete(
                request_url, params=self.__query_params, headers=headers, timeout=5
            )
            return response.json()
        except Exception as e:
            return {
                "status": False,
                "error": "Unable to delete data. Error:" + str(e),
            }

    def list_databases(self) -> dict:
        request_url = self.__api_url + "/db/databases"
        headers = {"accept": "application/json"}
        try:
            response = requests.get(request_url, headers=headers, timeout=5)
            return response.json()
        except Exception as e:
            return {
                "status": False,
                "error": "Unable to retrieve data. Error:" + str(e),
            }

    def list_tables_in_db(self, db_name: str = None) -> dict:
        if not db_name:
            return {"status": False, "error": "You did not provide a database name"}

        request_url = self.__api_url + "/db/" + db_name + "/tables"
        headers = {"accept": "application/json"}
        try:
            response = requests.get(request_url, headers=headers, timeout=5)
            return response.json()
        except Exception as e:
            return {
                "status": False,
                "error": "Unable to retrieve data. Error:" + str(e),
            }

    def from_db(self, db_name: str = None):
        if db_name:
            self.__db_name = db_name
        return self

    def into_db(self, db_name: str = None):
        if db_name:
            self.__db_name = db_name
        return self

    def from_table(self, table_name: str = None):
        if table_name:
            self.__table_name = table_name
        return self

    def into_table(self, table_name: str = None):
        if table_name:
            self.__table_name = table_name
        return self

    def where(self, col_name: str = None, operator: str = None, col_val: any = None):
        if operator in self.__operator_map:
            self.__where_query.append(
                col_name + "," + self.__operator_map[operator] + "," + str(col_val)
            )
        return self

    def or_where(self, col_name: str = None, operator: str = None, col_val: any = None):
        if operator in self.__operator_map:
            self.__or_where_query.append(
                col_name + "," + self.__operator_map[operator] + "," + str(col_val)
            )
        return self

    def per_page(self, per_page: int = 0):
        if per_page > 0:
            self.__per_page = per_page
        return self

    def page(self, page: int = 0):
        if page > 0:
            self.__page = page
        return self

    def sort_by(self, col_name: str = None, direction: str = None):
        if direction in self.__sort_order:
            self.__sort_by_list.append(col_name + ":" + direction)
        return self

    def select(self) -> dict:
        self.__assemble_query()
        return self.__make_select_request()

    def select_by_id(self, mongo_id: str = None):
        return self.__make_select_by_id_request(mongo_id)

    def update(self, data: Union[dict | list]) -> dict:
        self.__assemble_query()
        return self.__make_update_request(data)

    def update_by_id(self, mongo_id: str = None, data: Union[dict, list] = None):
        return self.__make_update_request_by_id(mongo_id, data)

    def insert(self, data: Union[dict, list] = None):
        return self.__make_insert_request(data)
    
    def insert_if(self, data : Union[dict, list]):
        self.__assemble_query()
        return self.__make_insert_if_request(data)
    
    def delete(self):
        self.__assemble_query()
        return self.__make_delete_request()

    def delete_by_id(self, mongo_id: str = None) -> dict:
        return self.__make_delete_by_id_request(mongo_id)

    def delete_database(self, db_name: str = None) -> dict:
        if not db_name:
            return {"status": False, "error": "You did not provide a database name"}

        request_url = self.__api_url + "/db/" + db_name + "/delete"
        headers = {"accept": "application/json"}
        try:
            response = requests.delete(request_url, headers=headers, timeout=5)
            return response.json()
        except Exception as e:
            return {
                "status": False,
                "error": "Unable to delete data. Error:" + str(e),
            }

    def delete_tables_in_db(self, db_name: str = None, table_name: str = None):
        if not table_name and not db_name:
            return {
                "status": False,
                "error": "You did not provide a valid database + table / collection name.",
            }

        request_url = self.__api_url + "/db/" + db_name + "/" + table_name + "/delete"
        headers = {"accept": "application/json"}
        try:
            response = requests.delete(request_url, headers=headers, timeout=5)
            return response.json()
        except Exception as e:
            return {
                "status": False,
                "error": "Unable to delete data. Error:" + str(e),
            }