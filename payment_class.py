#Class for Payment
#This class contains methods for payment processing, reminders and penalties.
class Payment:
    def __init__(self, payment_id, policyholder_id, product_id, amount, status='pending'):
        self.payment_id = payment_id
        self.policyholder_id = policyholder_id
        self.product_id = product_id
        self.amount = amount
        self.status = status

    def process(self):
        self.status = 'completed'
        print(f"Payment {self.payment_id} for Policyholder {self.policyholder_id} has been processed.")

    def remind(self):
        print(f"Reminder sent for Payment {self.payment_id} to Policyholder {self.policyholder_id}.")

    def penalize(self):
        print(f"Penalty applied for Payment {self.payment_id} for Policyholder {self.policyholder_id}.")

    def __str__(self):
        return f"Payment[ID: {self.payment_id}, PolicyholderID: {self.policyholder_id}, ProductID: {self.product_id}, Amount: {self.amount}, Status: {self.status}]"

