import random
import datetime
class customer_details:
    __current_ordersid=[]
    __completed_ordersid=[]
    def __init__(self):
        self.__customer_id = "cus"+str(random.randint(123456789,987654321))
    def set_current_orders(self,items):
        self.__current_ordersid.append(items)
    def get_customer_id(self):
        return self.__customer_id
    def update_order_status(self,order_id):
        if order_id in self.__current_ordersid:
            self.__completed_ordersid.append(order_id)
            self.__current_ordersid.remove(order_id)
        else:
            print("The order id is wrong")
    def get_customer_current_orders(self):
        return self.__current_ordersid
    def get_customer_completed_orderid(self):
        return self.__completed_ordersid
    