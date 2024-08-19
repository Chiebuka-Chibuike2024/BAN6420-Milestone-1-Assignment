#Policyholder demonstration
#Import the 3 classes

from Policyholder import Policyholder
from product_class import Product
from payment_class import Payment

#Products
product1 = Product(product_id=1, name="Auto Insurance", amount=10000)
product2 = Product(product_id=2, name="Home Insurance", amount=3000)

#Policyholders
policyholder1 = Policyholder(policyholder_id=1, name="Victoria Chibuike", email="vickylove@hot.com")
policyholder2 = Policyholder(policyholder_id=2, name="Daniel Briggs", email="danbriggs@hot.com")

#Payments
payment1 = Payment(payment_id=1, policyholder_id=1, product_id=1, amount=10000)
payment2 = Payment(payment_id=2, policyholder_id=2, product_id=2, amount=3000)

#Show Policyholders and Product Details
print(policyholder1)
print(policyholder2)
print(product1)
print(product2)

# Demonstrating Payments
payment1.process()
payment2.process()

# Display Payment Details
print(payment1)
print(payment2)





