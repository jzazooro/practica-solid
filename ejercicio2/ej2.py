class DataBaseManager():
    def __init__(self, connection_string):
        self.connection_string=connection_string

class Authenticator():
    def __init__(self, user_database):
        self.user_database=user_database

class OrderManager():
    def __init__(self, api_key):
        self.api_key=api_key

class PaymentProcessor():
    def __init__(self, database_manager, authenticator, order_manager):
        self.database_manager=database_manager
        self.authenticator=authenticator
        self.order_manager=order_manager