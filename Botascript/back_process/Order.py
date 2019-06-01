import json #pour plus tard
from datetime import datetime
from datetime import timedelta 
from .DB import *
from ast import literal_eval

default_order_log = "[DEFAULT - LOG] Script did not noticed anything."


class Order:

	def __init__(self, order_data):
		
		############### BENJAMIN : Interesting ###############
		self.tag =			order_data[6]
		self.args = 		json.loads(order_data[7])
		suppl_data = self._get_network_and_logins(order_data)
		self.network = 		suppl_data[2]
		self.login = 		suppl_data[0]
		self.password = 	suppl_data[1]
		#####################################################


		################# BACK END : Not interesting #############################
		self.id = 			order_data[0]
		self.intervalle = 	order_data[3]
		self.log =			default_order_log
		self.alive =		bool(order_data[10])
		self.exectime = 	datetime.strptime(order_data[4], '%Y-%m-%d %H:%M:%S')
		self.endtime =		datetime.strptime(order_data[5], '%Y-%m-%d %H:%M:%S')
		self.realized_already_called = False 		#Securite contre doublon
		##########################################################################


	
	def logs(self,log_message):
		""" FEED logs attribute of this object

		INPUT:	String to add in logs. Begin with SUCCESS::: or WARNING::: or ERROR:::
		OUTPUT: Ø #Add it to .log attribute of this object

		PS: Database is not yet notified ! Please call .realized() to notify the db.
		"""

		if self.log == default_order_log : 
			self.log = ""
		self.log += log_message + ";"



	def realized(self, message = "DEFAULT"):
		""" SAVE order's status and its logs in database
			
		INPUT:	Ø OR String that will replace .log attribute
		OUTPUT: Ø #Database modification.

		PS: Compute order's new data itself.
		PS: You can use it only once !
		"""

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

		self.realized_already_called = True #Order realized, security ON !

#####################################################################################
################################## DON'T TOUCH ######################################
#####################################################################################

	def _get_network_and_logins(self, order_data):
		"""GET logins from database

			INPUT:	User_id and Network_id
			OUTPUT: tuple of 3 values : network_login, network_password, network_name

			PS: Used only at order's creation.
		"""

		conn = sqlite3.connect(myDB)
		c = conn.cursor()
		params = (order_data[1], order_data[2])
		res = c.execute('SELECT network_login, network_password, networks.network_name FROM accounts JOIN networks ON networks.id = accounts.network_id  WHERE user_id = ? AND network_id = ?', params)
		for answer in res:
			return answer



	def __str__(self):
		return """
		id\t\t\tintervalle\t\t\texectime\t\t\tendtime\t\t\tTag d'ordre\
		\t\t\tArguments\t\t\talive
		{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}
		""".format(
			self.id, 
			self.intervalle,
			self.exectime, 
			self.endtime, 
			self.tag, 
			self.args, 
			self.alive)



	def __repr__(self):
		return self.__str__()



	def _save(self):
		""" SAVE order's state.

		INPUT: 	Ø
		OUTPUT: Ø #Database modification.

		PS: Used by .realized() method.
		"""

		conn = sqlite3.connect(myDB)
		c = conn.cursor()
		params = (self.exectime, self.alive , self.id)
		c.execute('UPDATE orders SET `exectime` = ?, `alive` = ? WHERE id=?', params)
		conn.commit()
		conn.close()


	
	def _save_log_in_db(self,message="DEFAULT"):
		""" SAVE order's log or message passed to .realized() method in db.

		INPUT:	Ø OR String passed to .realized()
		OUTPUT: Ø #Database modification.

		PS: Used by .realized() method.
		"""

		message = self.log if message == "DEFAULT" else message
		conn = sqlite3.connect(myDB)
		c = conn.cursor()

		rightnow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		c.execute("INSERT INTO logs (order_id, exectime, message, created_at, updated_at) VALUES (?,?,?, ?, ?)",(self.id, rightnow, message, rightnow, rightnow))
		conn.commit()
		conn.close()




