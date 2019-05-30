from Orders import Orders
import os

def resetDB():
	os.system('cd .. && cd Botaserver && rake db:drop && rake db:create && rake db:migrate && rake db:seed')

if __name__ == '__main__':
	
	print("=================== Some debugging stuff ===================")
	

else:

	#Only available for script importing Interface

	def launchTutoriel():
		orders = Orders()
		#0 - Actuellement l'objet orders est vide, il n'y a aucun ordre dedans
		print("\n\n===================== 0 ==========================\n\n")
		print(orders)

		
		#1 - Il est possible de parcourir les ordres très facilement
		print("\n\n===================== 1 ==========================\n\n")
		for order in orders:
			print(order)
		print("Nb: aucun ordre s'affiche, car notre liste d'ordres est encore vide.")
		

		#2 - Récupérer les ordres qui sont actuellement à faire avec .taff()
		print("\n\n===================== 2 ==========================\n\n")
		orders.taff()
		print(orders)
		for order in orders:
			print(order)
		

		#3 - Les ordres ont préchargé toutes les infos qui te sont nécessaires. Par exemple:
		print("\n\n===================== 3 ==========================\n\n")
		example = orders._getSample()
		print("Réseaux d'action 	: {}".format(example.network)) #FALSE
		print("Logs Utilisateur 	: Login: {} | Password: {} ".format(example.login, example.password)) #FALSE
		print("Tag de l'ordre 		: {}".format(example.tag))
		print("Arguments de l'ordre : {}".format(example.args))

		
		#4 - Pendant l'éxecution, tu peux avoir besoin plusieurs fois de remplir les logs pour affiner l'information
		print("\n\n===================== 4 ==========================\n\n")
		example.logs("SUCCESS:: 100 personnes ont été ajoutés.")
		example.logs("WARNING:: Il semble que Linkedin ai bloqué temporairement l'ajout de contact.")
		#Ici, les logs final contiendront les deux informations
		print("Rien de visuel. 		Cf. les commentaires du code.")


		#5 - A la fin de l'execution d'un ordre, tu notifies la base de données qu'il a été effectué
		print("\n\n===================== 5 ==========================\n\n")
		example.realized()
			#Sans argument, les logs relative à l'ordre sont envoyées à la DB
			#Avec argument, les logs relative à l'ordre sont totalement remplacées :  example.realized("Fail:: Ca n'a pas marché !")
		print("Rien de visuel. 		Cf. les commentaires du code.")


		#6 - Après avoir réalisé tous les ordres, une bonne pratique est de marquer la liste d'ordres comme finie
		print("\n\n===================== 6 ==========================\n\n")
		orders.finished()
		#Cela appelle .realized() sur tous les ordres. Pratique, si l'on en oublie un !
		print("Rien de visuel. 		Cf. les commentaires du code.")
		