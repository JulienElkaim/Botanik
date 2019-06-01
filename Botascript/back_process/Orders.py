from .Order import Order, datetime #S'assurer que c'est le meme datetime utilise
from .DB import *

class Orders:

	def __init__(self):
		self._orders_list = []
		self.pos = 0
	

	
	def getWork(self):
		""" GET list of orders left to execute according to the database
		INPUT: 	Ø
		OUTPUT: Ø #it modifies __orders_list

		"""

		self._orders_list = []
		conn = sqlite3.connect(myDB)
		c = conn.cursor()

		right_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		params =(True, right_now,)
		res = c.execute("SELECT* FROM orders WHERE alive = ? AND exectime <= ? ;", params)

		for order_data in res :
			order = Order(order_data)
			self._orders_list.append(order)

		conn.close()



	def finished(self):
		""" NOTIFY database of the end of execution for these orders.
		INPUT:	Ø
		OUTPUT: Ø

		PS: Call realized() method on each order.
		Let each order notify database of its changes and its logs.
		"""

		for order in self:
			order.realized();

		self._orders_list = []


	
	def __iter__(self):
		""" USED by iterators to begin parsing

		INPUT: 	Ø
		OUTPUT: Ø
		"""

		self.pos = 0
		return self



	def __next__(self):
		""" USED by iterators to parse this object

		INPUT: 	Ø
		OUTPUT: Ø
		"""

		if self.pos < len(self._orders_list) :
			self.pos +=1
			return self._orders_list[self.pos - 1]
		else:
			raise StopIteration



	def __str__(self):
		""" SHOW number of orders available 
		
		INPUT:	Ø
		OUTPUT: String explaining how many orders are to execute.
		
		PS: Called when using print() on this object.
		"""

		return "Je possede actuellement {} ordres a executer.".format(len(self._orders_list))



	
	def _getSample(self):
		""" CREATE a uniq order to illustrate a point in the tutorial
		
		INPUT:	Ø
		OUTPUT: Objet instance de la Class Order()
		
		PS: Never call this method.
		"""

		if len(self._orders_list) > 0:

			return self._orders_list[0]

		else:
			order_data = (1, 1, 1, 1814400, '2019-05-30 04:05:06', 
				'2020-05-30 04:05:06', 'ADD', 
				'{"Until": 500}', '2019-05-30 17:10:23.766200', 
				'2019-05-30 17:10:23.766200', 1)
			
			return Order(order_data)


