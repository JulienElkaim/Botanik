import json #pour plus tard
from datetime import datetime
from datetime import timedelta 
from DB import *

default_order_log = "Take it easy, tutti frutti !"

class Order:


	def __init__(self, order_data):
		self.id = 			order_data[0]
		self.intervalle = 	order_data[3]
		self.exectime = 	datetime.strptime(order_data[4], '%Y-%m-%d %H:%M:%S')
		self.endtime =		datetime.strptime(order_data[5], '%Y-%m-%d %H:%M:%S')
		self.type =			order_data[6]
		self.args = 		order_data[7]
		self.alive =		bool(order_data[10])
		self.log =			default_order_log

		self.realized_already_called = False 		#Sécurité



	#Permet d'avoir une liste de log pour une seul et même éxécution
	def logs(self,log_message):
		if self.log == default_order_log : 
			self.log = ""
		self.log += log_message + ";"



	#Représente l'ordre sous forme à peu près cohérente de tableau
	def __str__(self):
		return """
		id\t\t\tintervalle\t\t\texectime\t\t\tendtime\t\t\tType d'ordre\t\t\tArguments\t\t\talive
		{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}
		""".format(self.id, self.intervalle, self.exectime, self.endtime, self.type, self.args, self.alive)

	def __repr__(self):
		return self.__str__()


	# Ordre réalisé, modifie les logs, et met à jour l'ordre. /!\ CALLABLE ONLY 1 TIME /!\
	def realized(self, message = "DEFAULT"):
		if self.realized_already_called: #Sécurité
			return false

		if self.intervalle == 0:		#Tasks
			self.alive = False

		else:							#Routines
			next_exec = self.exectime + timedelta(seconds=self.intervalle)
			
			if next_exec > self.endtime:
				self.alive = False
			else:
				self.exectime = next_exec
				
		self.save()
		message = self.log if message == "DEFAULT" else message
		self.write_log(message)

	#Sauvegarde l'état actuel de l'ordre
	def save(self):
		conn = sqlite3.connect(myDB)
		c = conn.cursor()
		t = (self.exectime, self.alive , self.id)
		c.execute('UPDATE orders SET `exectime` = ?, `alive` = ? WHERE id=?', t)
		conn.commit()
		conn.close()


	# Ecrit dans les logs
	def write_log(self,message="DEFAULT"):
		message = self.log if message == "DEFAULT" else message
		conn = sqlite3.connect(myDB)
		c = conn.cursor()

		rightnow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		c.execute("INSERT INTO logs (order_id, exectime, message, created_at, updated_at) VALUES (?,?,?, ?, ?)",(self.id, rightnow, message, rightnow, rightnow))
		conn.commit()
		conn.close()




