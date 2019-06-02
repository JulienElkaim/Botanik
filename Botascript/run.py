from back_process.Interface import *

#===============/!\ IGNORE IT /!\=======================
ordersToExec = Orders() # Orders list creation, empty.
ordersToExec.getWork() # Fill the list with orders to execute.
#=======================================================



##############################################################################
###################### PARTIE MODIFIABLE EN-DESSOUS ##########################
##############################################################################




# ============== BENJAMIN ! Choisir un mode ===================
MODE = { "CRASH": False, "DEV": True, "PROD": False}
# =============================================================




if MODE["CRASH"]:
	
	getFakeDB(); #Erase DB and create fake records.
	print("\n\n=========== THIS IS A WAR ZONE =============\n\n")
	
	# Dirty stuff 
	


if MODE["DEV"]:
	print("\n\n=========== DEVELOPMENT MODE ===========\n\n")

	for order in ordersToExec:
		# /!\ Ton code ICI /!\
		pass
		

	ordersToExec.finished() #Ensure to notify database 




if MODE["PROD"]:
	print("\n\n=========== PRODUCTION ================\n\n")
	
	for order in ordersToExec:
		# /!\ Ton code ICI /!\
		pass
		

	ordersToExec.finished() #Ensure to notify database 






