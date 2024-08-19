#Product Class
#Contains methods for creating, updating, suspending/removing policy products
class Product:
    def __init__(self, product_id, name, amount, status='active'):
        self.product_id = product_id
        self.name = name
        self.amount = amount
        self.status = status

    def update(self, name=None, amount=None):
        if name:
            self.name = name
        if amount:
            self.amount = amount
        print(f"Product {self.product_id} is updated.")

    def suspend(self):
        self.status = 'suspended'
        print(f"Product {self.name} has been suspended.")

    def __str__(self):
        return f"Product[ID: {self.product_id}, Name: {self.name}, Amount: {self.amount}, Status: {self.status}]"










