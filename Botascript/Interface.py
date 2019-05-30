import json
from datetime import datetime
from datetime import timedelta 
import sqlite3



class Order:
	def __init__(self, order_data):
		self.id = 			order_data[0]
		self.intervalle = 	order_data[3]
		self.exectime = 	datetime.strptime(order_data[4], '%Y-%m-%d %H:%M:%S')
		self.endtime =		datetime.strptime(order_data[5], '%Y-%m-%d %H:%M:%S')
		self.type =			order_data[6]
		self.args = 		order_data[7]
		self.alive =		 bool(order_data[10])

	def __str__(self):
		return """
		id\t\t\tintervalle\t\t\texectime\t\t\tendtime\t\t\tType d'ordre\t\t\tArguments\t\t\talive
		{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}
		""".format(
		 self.id,
		 self.intervalle,
		 self.exectime,
		 self.endtime,
		 self.type,
		 self.args,
		 self.alive)

	def __repr__(self):
		return self.__str__()

	# Note que l'ordre a été effectué, va modifier l'ordre et va inscrire le message de log
	def realized(self, message="Botanik is mad."):
		print(self.alive)
		if self.intervalle == 0:
			#Tasks
			print("hm")
			self.alive = False
		else:
			#Routines
			next_exec = self.exectime + timedelta(seconds=self.intervalle)
			if next_exec > self.endtime:
				#C'est fini
				self.alive = False
			else:
				self.exectime = next_exec
				#On va repartir

		self._saveit()
		print("finish")

	def _saveit(self):
		conn = sqlite3.connect('../Botaserver/db/development.sqlite3')
		c = conn.cursor()
		t = (self.exectime, self.alive , self.id)
		c.execute('UPDATE orders SET `exectime` = ?, `alive` = ? WHERE id=?', t)
		conn.commit()
		conn.close()
		



conn = sqlite3.connect('../Botaserver/db/development.sqlite3')
c = conn.cursor()

rez = c.execute("SELECT* FROM orders WHERE alive;")
orders=[]
for order in rez:
	orders.append(Order(order))


orders[1].realized()
# Save (commit) the changes
#conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()
