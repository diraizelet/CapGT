import random
import datetime
class order_details:
    def __init__(self, customer):
        self.__customer_id = customer.get_customer_id()
        self.assign_date_time()
        self.__order_id = "ref" + str(random.randint(123456789, 987654321))

    def get_order_id(self):
        return self.__order_id
    
    def assign_date_time(self):
        self.__date_time=datetime.datetime.now()
    def get_date_time(self):
        return self.__date_time
    def get_customer_id(self):
        return self.__customer_id
    