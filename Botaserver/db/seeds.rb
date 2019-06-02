# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)



#Create Fake Users
User.create([
	{username: "Julien Elkaim", password: "PizzaIsLife"},
	{username: "Benjamin Soulan", password: "CookieIsLife"}
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
	{user_id: 1, network_id: 1,network_login: "julien.linkedin@gmail.com", network_password: "JusDePommeLinkedin" },
	{user_id: 1, network_id: 2,network_login: "julien.instagram@gmail.com", network_password: "JusDePommeInstagram" },
	{user_id: 2, network_id: 1,network_login: "benjamin.linkedin@orange.fr", network_password: "BenjaminButtonLinkedin" },
	{user_id: 2, network_id: 2,network_login: "benjamin.instagram@orange.fr", network_password: "BenjaminButtonInstagram"},
	{user_id: 2, network_id: 3,network_login: "benjamin.facebook@orange.fr", network_password: "BenjaminButtonFacebook"},
	{user_id: 2, network_id: 4,network_login: "benjamin.twitter@orange.fr", network_password: "BenjaminButtonTwitter"}
])
#end


#Create Fake Orders ------ /!\ Changer les dates pour qu'elles soient utiles ! /!\
Order.create([

	#Julien veut ajouter 100 personnes, 
	#toutes les 3 semaines, 
	#sur LINKEDIN
	{user_id: 1, network_id: 1, intervalle: Order.convertTime("3 semaines"), exectime: DateTime.new(2019,5,29,4,5,6), endtime: DateTime.new(2020,5,30,4,5,6), order_tag: "ADD", order_args: '{"Until": 500}'},
	
	#Julien veut liker 50 personnes,
	#une seule fois,
	#sur INSTAGRAM
	{user_id: 1, network_id: 2, intervalle: 0, exectime: DateTime.new(2019,5,29,4,5,6), endtime: DateTime.new(2019,5,29,4,5,6), order_tag: "LIKE", order_args: '{"Until": 50}'},
	
	#Julien veut liker 10 postes,
	#CONDITION 1 : Créés par des personnes dont la description est exactement "Marketing de réseaux",
	#CONDITION 2 : Dont le corps de texte contient "Mon cher réseaux",
	#tous les 3 jours,
	#sur LINKEDIN
	{user_id: 1, network_id: 1, intervalle: Order.convertTime("3 jours"), exectime: DateTime.new(2019,5,29,4,5,6), endtime: DateTime.new(2019,5,30,4,5,6), order_tag: "LIKE", order_args: '{"Until": 10 ,"Fonction_match": "Marketing de réseaux", "Body_contains": "Mon cher réseaux"}'},
	
	#Benjamin veut liker 100 photo instagram,
	#CONDITION 1 : Dont la description contient un des # suivants : #TropPopulaire #PoissonRouge
	#tous les jours,
	#sur INSTAGRAM
	{user_id: 2, network_id: 2, intervalle: Order.convertTime("1 jour"), exectime: DateTime.new(2019,5,29,4,5,6), endtime: DateTime.new(2019,6,15,4,5,6), order_tag: "LIKE", order_args: '{"Until": 100 ,"Desc_match_or": ["#TropPopulaire","#PoissonRouge"]}'},
	
	#Benjamin veut ajouter autant de personnes possible,
	#toutes les 5 heures,
	#sur LINKEDIN
	{user_id: 2, network_id: 1, intervalle: Order.convertTime("5 heures"), exectime: DateTime.new(2019,5,29,4,5,6), endtime: DateTime.new(2020,6,15,4,5,6), order_tag: "ADD", order_args: '{}'},

])

Log.create(order_id: 1, exectime: DateTime.new(2000,5,30,4,5,6),  message: "SUCCESS:: Notifie d'un succès;")
Log.create(order_id: 1, exectime: DateTime.new(2000,5,30,4,5,7),  message: "SUCCESS:: Notifie d'un succès;WARNING:: Notifie d'une anomalie;")
Log.create(order_id: 1, exectime: DateTime.new(2000,5,30,4,5,8),  message: "FAIL:: Notifie d'un échec dans l'éxécution;")



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
