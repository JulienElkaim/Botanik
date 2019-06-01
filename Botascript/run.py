from Interface import *
TUTO_MODE = True 	#Set -> True during training stage. Otherwise, False.
DEV_MODE = False 	#Set -> True during development stage. Otherwise, False.
PROD_MODE = False 	#Set -> True during production stage. Otherwise, False.



orders = Orders() #Objet principal, une liste d'ordres




for order in orders:
	print(order)


if TUTO_MODE:
	
	
	print("\n\n=========== You are in TUTORIAL MODE =============\n\n")

	## Code de tutoriel
	resetDB()			#Goto the ../Botaserver/db/seeds.rb file to create fake records.
	launchTutoriel() 	#Goto Interface.py to see tutorial comments.
	#Comment above lines if necessary.

	

if DEV_MODE:
	print("\n\n=========== You are in DEVELOPMENT MODE ===========\n\n")
	## Code en developemment


if PROD_MODE:
	print("\n\n=========== You are in PRODUCTION ================\n\n")
	## Code en production