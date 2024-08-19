                                      POLICY MANAGEMENT SYSTEM FOR AN INSURANCE COMPANY

OVERVIEW:

- This system enables the insurance company to manage Policyholders, Products and Payments. It allows Policy Managers to perform tasks such as; registering, suspending, re-activating Policyholders, etc.

- Each class resides in its own file, and they are imported into the script (Demonstration_Milestone.py) to demonstrate how they interact.

- The Demonstration_Milestone.py script creates instances of Policyholder, Product, and Payment; processes payments and displays information.

STRUCTURE:
1) Policyholder Class: It is stored in the file "Policyholder.py". Its methods are:

a) __init__(self, policyholder_id, name, email, status): Initializes a new policyholder with a unique ID, name, email and assigns the status "active" .
b) suspend(self): Suspends the policyholder.
c) reactivate(self): Reactivates a suspended policyholder.

2) Product Class: It is stored in the file "product_class.py". Its methods are:
a) __init__(self, product_id, name, amount, status='active'): Initializes a new product with a unique ID, name, amount and assigns the status "active".
b) update(self, name=None, amount=None):Updates the product's name/amount.
c) suspend(self):Suspends the product.

3) Payment Class: Stored in the file "payment_class.py". Its methods are:
a) __init__(self, payment_id, policyholder_id, product_id, amount):Initializes new payment method.
b) process(self):Processes payment.
c) remind(self): sends a reminder if payment is not complete.
d) penalize(self): It applies Penalties if payment is overdue.

DEMONSTRATION:

- You can see the system in action by running the "Demonstration_Milestone.py" file. The demonstration includes:

a)Creating products and policyholders.

b)Processing payments for the policyholders.

c)Displaying the details of policyholders and products.

REQUIREMENTS:
- Python 3.x; PyCharm Professional(IDE)

README_Milestone 1: Documentation on how to use the code.
