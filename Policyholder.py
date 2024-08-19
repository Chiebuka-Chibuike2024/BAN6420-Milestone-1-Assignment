#Policyholder class
#Method to "register", "suspend" and "re-activate" Policyholders
class Policyholder:
    def __init__(self, policyholder_id, name, email, status='active'):
        self.policyholder_id = policyholder_id
        self.name = name
        self.email = email
        self.status = status

    def suspend(self):
        self.status = 'suspended'
        print(f"Policyholder {self.name} has been suspended.")

    def reactivate(self):
        self.status = 'active'
        print(f"Policyholder {self.name} is reactivated.")

    def __str__(self):
        return f"Policyholder[ID: {self.policyholder_id}, Name: {self.name}, Email: {self.email}, Status: {self.status}]"






