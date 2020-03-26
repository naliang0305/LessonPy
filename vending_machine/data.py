class Drink:  #Class命名大寫開頭
    def __init__(self, new_name, new_price):
        self.name = new_name
        self.price = new_price

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.name = new_name

    def get_price(self):
        return self.__price

