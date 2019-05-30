from Interface import *


orders = Orders()
for order in orders:
	print(order)

print("========= AFTER calling .taff() method")

orders.taff()
for order in orders:
	print(order)