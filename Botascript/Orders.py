from Order import Order, datetime #S'assurer que c'est le meme datetime utilise
from DB import *

class Orders:

	def __init__(self):
		self.orders_list = []
		self.pos = 0
		# self.taff()
    

	#Recuperes la liste des ordres a effectuer ce tour ci
	def taff(self):
		self.orders_list = []

		conn = sqlite3.connect(myDB)
		c = conn.cursor()

		right_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		params =(True, right_now,)
		res = c.execute("SELECT* FROM orders WHERE alive = ? AND exectime <= ? ;", params)

		for order_data in res :
			order = Order(order_data)
			self.orders_list.append(order)


		conn.close()

	# Tous les ordres sont acheves, lancer un realized global pour s'assurer que tout a ete update dans la DB.
	def finished(self):
		for order in self:
			order.realized();


	#ITERATION, initialization des variables de parcours de liste
	def __iter__(self):
		self.pos = 0
		return self

	#ITERATION, comportement a chaque tour du parcours
	def __next__(self):
		if self.pos < len(self.orders_list) :
			self.pos +=1
			return self.orders_list[self.pos - 1]
		else:
			raise StopIteration

	def __str__(self):
		return "Je possede actuellement {} ordres a executer.".format(len(self.orders_list))



	# SALE ! Juste la pour les besoins du tutoriel, ne jamais utiliser sinon.
	def _getSample(self):
		if len(self.orders_list) > 0:
			return self.orders_list[0]
		else:
			order_data = (1, 1, 1, 1814400, '2019-05-30 04:05:06', '2020-05-30 04:05:06', 'ADD', "{'Until': 500}", '2019-05-30 17:10:23.766200', '2019-05-30 17:10:23.766200', 1)
			return Order(order_data)


