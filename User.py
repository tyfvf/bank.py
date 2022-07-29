class User:
    all = []
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        
        temp = [self.__username, self.__password]

        self.all.append(temp)