class MysqlRepository:
    def __init__(self) -> None:
        self.__data = {
            "Weverton": "Mata"
        }
        
    def select_by_name(self, name:str) -> None:
        if name in self.__data:
            return self.__data[name]
        return None
        