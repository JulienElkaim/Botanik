from .Orders import Orders
import os

def getFakeDB():
	import os
	dirname = os.path.dirname(__file__)

	botanik = os.path.join(dirname, '../..')
	
	os.system('cd {} && cd Botaserver && rake db:drop && rake db:create\
	 && rake db:migrate && rake db:seed'.format(botanik))

if __name__ == '__main__':
	
	print("=================== Some debugging stuff ===================")
	
	####################################################################
	###################### ZONE POUR DEBUGGING #########################
	####################################################################

else:

	#Only available for script importing Interface

	def launchTutoriel():
		orders = Orders()
		#0 - Actuellement l'objet orders est vide, il n'y a aucun ordre dedans
		print("\n\n===================== 0 ==========================\n\n")
		print(orders)

		
		#1 - Il est possible de parcourir les ordres tres facilement
		print("\n\n===================== 1 ==========================\n\n")
		for order in orders:
			print(order)
		print("Nb: aucun ordre s'affiche, car notre liste d'ordres est encore vide.")
		

		#2 - Recuperer les ordres qui sont actuellement a faire avec .taff()
		print("\n\n===================== 2 ==========================\n\n")
		orders.getWork()
		print(orders)
		for order in orders:
			print(order)
		

		#3 - Les ordres ont precharge toutes les infos qui te sont necessaires. Par exemple:
		print("\n\n===================== 3 ==========================\n\n")
		example = orders._getSample()
		print("Reseaux d'action 	: {}".format(example.network)) #FALSE
		print("Logs Utilisateur 	: Login: {} | Password: {} ".format(example.login, example.password)) #FALSE
		print("Tag de l'ordre 		: {}".format(example.tag))
		print("Arguments de l'ordre : {}".format(example.args))

		
		#4 - Pendant l'execution, tu peux avoir besoin plusieurs fois de remplir les logs pour affiner l'information
		print("\n\n===================== 4 ==========================\n\n")
		example.logs("SUCCESS:: 100 personnes ont ete ajoutes.")
		example.logs("WARNING:: Il semble que Linkedin ai bloque temporairement l'ajout de contact.")
		#Ici, les logs final contiendront les deux informations
		print("Rien de visuel. 		Cf. les commentaires du code.")


		#5 - A la fin de l'execution d'un ordre, tu notifies la base de donnees qu'il a ete effectue
		print("\n\n===================== 5 ==========================\n\n")
		example.realized()
			#Sans argument, les logs relative a l'ordre sont envoyees a la DB
			#Avec argument, les logs relative a l'ordre sont totalement remplacees :  example.realized("Fail:: Ca n'a pas marche !")
		print("Rien de visuel. 		Cf. les commentaires du code.")


		#6 - Apres avoir realise tous les ordres, une bonne pratique est de marquer la liste d'ordres comme finie
		print("\n\n===================== 6 ==========================\n\n")
		orders.finished()
		#Cela appelle .realized() sur tous les ordres. Pratique, si l'on en oublie un !
		print("Rien de visuel. 		Cf. les commentaires du code.")
		