class LocatorTuple:
    def __init__(self, method: str, query: str):
        self.__method = method
        self.__query = query

    def to_tuple(self):
        return self.__method, self.__query
