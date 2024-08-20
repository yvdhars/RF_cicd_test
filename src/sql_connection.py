from abc import ABC, abstractmethod


class sql_connction_abstract(ABC):

    @abstractmethod
    def connect_sql(self, connection_string: str) ->None:
        pass

    @abstractmethod
    def run_query(self, query: str) ->None:
        pass