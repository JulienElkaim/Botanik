import json #pour plus tard
from datetime import datetime
from datetime import timedelta 
from DB import *

default_order_log = "Take it easy, tutti frutti !"

class Order:


	def __init__(self, order_data):
		#Variables pour benjamin
		self.id = 			order_data[0]
		self.tag =			order_data[6]
		self.args = 		order_data[7]
		self.alive =		bool(order_data[10])
		self.log =			default_order_log

		suppl_data = self.get_network_and_logins(order_data)
		self.network = 		suppl_data[2]
		self.login = 		suppl_data[0]
		self.password = 	suppl_data[1]

		#Variables pour le back
		self.intervalle = 	order_data[3]
		self.exectime = 	datetime.strptime(order_data[4], '%Y-%m-%d %H:%M:%S')
		self.endtime =		datetime.strptime(order_data[5], '%Y-%m-%d %H:%M:%S')
		self.realized_already_called = False 		#Securite contre doublon



	def get_network_and_logins(self, order_data):
		conn = sqlite3.connect(myDB)
		c = conn.cursor()
		params = (order_data[1], order_data[2])
		res = c.execute('SELECT network_login, network_password, networks.network_name FROM accounts JOIN networks ON networks.id = accounts.network_id  WHERE user_id = ? AND network_id = ?', params)
		for answer in res:
			return answer


	#Permet d'avoir une liste de log pour une seul et meme execution
	def logs(self,log_message):
		if self.log == default_order_log : 
			self.log = ""
		self.log += log_message + ";"



	#Represente l'ordre sous forme a peu pres coherente de tableau
	def __str__(self):
		return """
		id\t\t\tintervalle\t\t\texectime\t\t\tendtime\t\t\tTag d'ordre\t\t\tArguments\t\t\talive
		{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}
		""".format(self.id, self.intervalle, self.exectime, self.endtime, self.tag, self.args, self.alive)

	def __repr__(self):
		return self.__str__()


	# Ordre realise, modifie les logs, et met a jour l'ordre. /!\ CALLABLE ONLY 1 TIME /!\
	def realized(self, message = "DEFAULT"):
		
		if self.realized_already_called: #Securite contre doublon
			return False

		if self.intervalle == 0:		#Tasks
			self.alive = False

		else:							#Routines
			next_exec = self.exectime + timedelta(seconds=self.intervalle)
			
			if next_exec > self.endtime:
				self.alive = False
			else:
				self.exectime = next_exec
				
		self._save()
		message = self.log if message == "DEFAULT" else message
		self._save_log_in_db(message)

		self.realized_already_called = True #Ordre realise, securite ON

	#Sauvegarde l'etat actuel de l'ordre
	def _save(self):
		conn = sqlite3.connect(myDB)
		c = conn.cursor()
		params = (self.exectime, self.alive , self.id)
		c.execute('UPDATE orders SET `exectime` = ?, `alive` = ? WHERE id=?', params)
		conn.commit()
		conn.close()


	# Ecrit dans les logs
	def _save_log_in_db(self,message="DEFAULT"):
		message = self.log if message == "DEFAULT" else message
		conn = sqlite3.connect(myDB)
		c = conn.cursor()

		rightnow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		c.execute("INSERT INTO logs (order_id, exectime, message, created_at, updated_at) VALUES (?,?,?, ?, ?)",(self.id, rightnow, message, rightnow, rightnow))
		conn.commit()
		conn.close()




