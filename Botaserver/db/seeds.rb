# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

mode = "DEMO"

#Create Fake Users
User.create([
	{username: "Victor", password: "ciarletta", email:"victor.ben-ami@hotmail.com"},
	{username: "Julien", password: "ciarletta", email: "julienelk@gmail.com"}
])

# end


#Create Fake Networks
Network.create([
	{network_name:"Linkedin"},
	{network_name:"Instagram"},
	{network_name:"Facebook"},
	{network_name:"Twitter"}
])
#end


#Create Fake Accounts
Account.create([
	{user_id: 1, network_id: 1,network_login: "victor.ben-ami@hotmail.com", network_password: "Vo0RdQBkNZrB2usB9Hum" },
	{user_id: 2, network_id: 1,network_login: "julienelk@gmail.com", network_password: "Spraide" },
	{user_id: 2, network_id: 2,network_login: "julienelk@gmail.com", network_password: "Spraide"}

])
#end

# {"until": 5,
# "lieux": ["France", "Royaume-uni"],
# "current_e": ["bn"],
# "former_e": ["societe ge", "rotschild"],
# "sector": ["banque"],
# "school": ["hec paris", "ICN"]
# DateTime.new(2019,6,9,15,59,59)

Order.create([

	#Julien veut ajouter 100 personnes,
	#toutes les 3 semaines,
	#sur LINKEDIN

	# ===== VICTOR
	# 1
	#Poster une annonce de recrutement UNE FOIS dans 5 heures [LOG] NO LOG !
	# {user_id: 1, title: "Poster une annonce de recrutement", network_id: 1, intervalle: 0, exectime: (Time.now.utc + Order.convertTime("5 heures")).change(usec: 0), endtime: (Time.now.utc + Order.convertTime("5 heures")).change(usec: 0), order_tag: "POST", order_args: '{"message": "Bonjour, mon équipe est actuellement à la recherche du stagiaire de nos rêves...""}'},

	# ===== JULIEN
	# 2
	#Ajouter des amis tous les 4 heures [LOG] Imaginer que il a déjà fait 3 logs, VIVANT !
	# {user_id: 2, title: "Concours I-Lab: Max de contact !", network_id: 1, intervalle: Order.convertTime("4 heures"), exectime: (Time.now.utc + Order.convertTime("4 heures")).change(usec: 0) , endtime: (Time.now.utc + Order.convertTime("1 semaines")).change(usec: 0), order_tag: "ADD", order_args: '{"until": 15}'},

	# 3
	#Demander UNE FOIS à tous mes contacts de liker mon projet [LOG] C'était y a une semaine, MORT !
	# {user_id: 2, title: "Demander de liker mon projet", network_id: 3, intervalle: 0, exectime: (Time.now.utc - Order.convertTime("1 semaines")).change(usec: 0), endtime: (Time.now.utc - Order.convertTime("1 semaines")).change(usec: 0), order_tag: "MSG", order_args: '{"contact": "all", "until": 10, "msg": "Bonjour !\n Pourrais tu prendre deux secondes pour liker mon projet sur I-Lab?"}', alive: false},

	# 4
	#Poster son CV sur Linkedin [LOG] Imaginer qu'il a déjà fait trois logs, MORT !
	# {user_id: 2, title: "Poster son CV", network_id: 1, intervalle: Order.convertTime("1 jour"), exectime: (Time.now.utc - Order.convertTime("7 jours")).change(usec: 0), endtime: (Time.now.utc - Order.convertTime("7 jours")).change(usec: 0), order_tag: "POST", order_args: '{"message": "Cher réseaux, actuellement en M2 Informatique aux Mines Nancy..."}', alive: false},

  # 5
  # Copie de celui juste en dessous pour avoir un truc a exec
  # {user_id: 1, title: "Poster un hello world !", network_id: 1, intervalle: 0, exectime: Time.now.utc.change(usec: 0), endtime: Time.now.utc.change(usec: 0), order_tag: "POST", order_args: '{"message": "Bonjour\n le monde !"}'},
  {user_id: 1, title: "Ajoute 10 pers toutes les 4 minutes!", network_id: 1, intervalle: Order.convertTime("4 minutes"), exectime: Time.now.utc.change(usec: 0) , endtime: (Time.now.utc + Order.convertTime("1 semaines")).change(usec: 0), order_tag: "ADD", order_args: {"until": 10}},
])



#Order 2
Log.create(order_id: 2, exectime: (Time.now.utc - Order.convertTime("8 heures")).change(usec: 0),  message: "SUCCESS:: Ajouts effectués;WARNING:: Seulement 13 personnes ajoutées.")
Log.create(order_id: 2, exectime: (Time.now.utc - Order.convertTime("4 heures")).change(usec: 0),  message: "SUCCESS:: Ajouts effectués;")
Log.create(order_id: 2, exectime: Time.now.utc.change(usec: 0),  message: "FAIL:: Linkedin vous interdit d'ajouter plus d'amis;")

#Order 3
Log.create(order_id: 3, exectime:(Time.now.utc - Order.convertTime("1 semaines")).change(usec: 0) ,  message: "SUCCESS:: Messages envoyés;WARNING:: Seulement 168 personnes ont reçu le message.")

#Order 4
Log.create(order_id: 4, exectime:(Time.now.utc - Order.convertTime("7 jours")).change(usec: 0),  message: "SUCCESS:: Message envoyé avec succès.")
Log.create(order_id: 4, exectime:(Time.now.utc - Order.convertTime("8 jours")).change(usec: 0),  message: "SUCCESS:: Message envoyé avec succès.")
Log.create(order_id: 4, exectime:(Time.now.utc - Order.convertTime("9 jours")).change(usec: 0),  message: "SUCCESS:: Message envoyé avec succès.")



#================ STUFF FOR EDITING =====================================
#Users created (id, username, password)
#Networks created (id, network_name)

#accounts created (id, user_id, network_id, network_login, network_password)
	#network_id et user_id referencés comme des FK : OK !
	#

#orders created (id, user_id, network_id, intervalle, exectime, endtime, order_tag, order_args)

#logs created (id, order_id, exectime, message)

# MAKE SOME EXEC STUFF
# ordre = Order.first
# puts ordre.user.accounts.where(network: ordre.network).first.network_password
# puts ordre.network.network_name

# puts "=========="

# puts Account.first.user.orders.first.order_tag
