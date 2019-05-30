from Order import Order, datetime #S'assurer que c'est le même datetime utilisé
from DB import *

class Orders:

	def __init__(self):
		self.orders_list = []
		self.pos = 0
		# self.taff()
    

	#Récupères la liste des ordres à effectuer ce tour ci
	def taff(self):
		self.orders_list = []

		conn = sqlite3.connect(myDB)
		c = conn.cursor()

		right_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		params =(False, right_now,)
		res = c.execute("SELECT* FROM orders WHERE alive = ? AND exectime <= ? ;", params)

		for order_data in res :
			order = Order(order_data)
			self.orders_list.append(order)


		conn.close()

	def finish(self):
		for order in self:
			order.realized();
	#ITERATION, initialization des variables de parcours de liste
	def __iter__(self):
		self.pos = 0
		return self

	#ITERATION, comportement à chaque tour du parcours
	def __next__(self):
		if self.pos < len(self.orders_list) :
			self.pos +=1
			return self.orders_list[self.pos - 1]
		else:
			raise StopIteration


