from redis import Redis
from .conn_options import conn_options

class RedisConnectionHandle:
    def __init__(self) -> None:
        self.__host = conn_options["HOST"]
        self.__port = conn_options["PORT"]
        self.__db = conn_options["DB"]
        self.__conn = None
    
    def connect(self) -> Redis:
        self.__conn = Redis(
            host=self.__host,
            port=self.__port,
            db=self.__db
        )
        return self.__conn
    
    def get_conn(self) -> Redis:
        return self.__conn