# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)



#Create Fake Users
User.create([
	{username: "Victor Ben-Ami", password: "ciarletta", email:"victor.ben-ami@hotmail.com"},
	{username: "Benjamin Soulan", password: "ciarletta", email: "benjamin.soulan@orange.fr"},
	{username: "Julien Elkaim", password: "ciarletta", email: "benjamin.soulan@orange.fr"}
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
	{user_id: 1, network_id: 2,network_login: "julien.instagram@gmail.com", network_password: "JusDePommeInstagram" },
	{user_id: 2, network_id: 1,network_login: "benjamin.linkedin@orange.fr", network_password: "BenjaminButtonLinkedin" },
	{user_id: 2, network_id: 2,network_login: "benjamin.instagram@orange.fr", network_password: "BenjaminButtonInstagram"},
	{user_id: 2, network_id: 3,network_login: "benjamin.facebook@orange.fr", network_password: "BenjaminButtonFacebook"},
	{user_id: 2, network_id: 4,network_login: "benjamin.twitter@orange.fr", network_password: "BenjaminButtonTwitter"}
])
#end

# {"until": 5,
# "lieux": ["France", "Royaume-uni"],
# "current_e": ["bn"],
# "former_e": ["societe ge", "rotschild"],
# "sector": ["banque"],
# "school": ["hec paris", "ICN"]
# DateTime.new(2019,6,9,15,59,59)

#Create Fake Orders ------ /!\ Changer les dates pour qu'elles soient utiles ! /!\
Order.create([

	#Julien veut ajouter 100 personnes, 
	#toutes les 3 semaines, 
	#sur LINKEDIN
	{user_id: 1, title: "Un ordre classique, a exec deux min apres", network_id: 1, intervalle: Order.convertTime("3 heures"), exectime: DateTime.new(2019,6,9,19,47,6), endtime: DateTime.new(2019,6,9,19,47,6), order_tag: "ADD", order_args: '{"until": 15}'},
	{user_id: 1, title: "Teste de former_e avec de sogé", network_id: 1, intervalle: Order.convertTime("3 minutes"), exectime: DateTime.new(2019,6,9,19,47,6), endtime: DateTime.new(2019,6,9,19,47,6), order_tag: "ADD", order_args: '{"until": 10, "former_e": ["societe ge"]}'},
	{user_id: 1, title: "ici on test lieux et former_e ensemble", network_id: 1, intervalle: Order.convertTime("1 heures"), exectime: DateTime.new(2019,6,9,19,47,6), endtime: DateTime.new(2019,6,9,19,47,6), order_tag: "ADD", order_args: '{"until": 10, "lieux": ["France"],"former_e": ["rotschild"]}'}
	#Julien veut liker 50 personnes,
	#une seule fois,
	#sur INSTAGRAM
	#{user_id: 1, title: "I love you all", network_id: 2, intervalle: 0, exectime: DateTime.new(2019,6,9,10,03,59), endtime: DateTime.new(2019,5,29,4,5,6), order_tag: "LIKE", order_args: '{"Until": 50}'},
	
	#Julien veut liker 10 postes,
	#CONDITION 1 : Créés par des personnes dont la description est exactement "Marketing de réseaux",
	#CONDITION 2 : Dont le corps de texte contient "Mon cher réseaux",
	#tous les 3 jours,
	#sur LINKEDIN
	#{user_id: 1, title:"Relations Marketing de réseaux", network_id: 1, intervalle: Order.convertTime("3 jours"), exectime: DateTime.new(2019,6,10,12,59,59), endtime: DateTime.new(2019,5,30,4,5,6), order_tag: "LIKE", order_args: '{"until": 10 ,"Fonction_match": "Marketing de réseaux", "Body_contains": "Mon cher réseaux"}'},
	
	#Benjamin veut liker 100 photo instagram,
	#CONDITION 1 : Dont la description contient un des # suivants : #TropPopulaire #PoissonRouge
	#tous les jours,
	#sur INSTAGRAM
	#{user_id: 2, title: "Tu m'likes j'te like !", network_id: 2, intervalle: Order.convertTime("1 jour"), exectime: DateTime.new(2019,5,29,4,5,6), endtime: DateTime.new(2019,6,14,4,2,6), order_tag: "LIKE", order_args: '{"until": 100 ,"Desc_match_or": ["#TropPopulaire","#PoissonRouge"]}'},
	
	#Benjamin veut ajouter autant de personnes possible,
	#toutes les 5 heures,
	#sur LINKEDIN
	#{user_id: 2, title: "Je prends tout le monde !", network_id: 1, intervalle: Order.convertTime("5 heures"), exectime: DateTime.new(2019,5,29,4,5,6), endtime: DateTime.new(2020,6,15,4,5,6), order_tag: "ADD", order_args: '{}'},

])
=begin
Log.create(order_id: 1, exectime: DateTime.new(2000,5,30,4,5,7),  message: "SUCCESS:: Notifie d'un succès;")
Log.create(order_id: 2, exectime: DateTime.new(2000,5,30,4,5,6),  message: "SUCCESS:: Vous avez réussi votre tâche. ;WARNING:: L'ordre a fini mais on s'est fait bloquer à 30 likes environ. Vérifiez si Instagram ne vous a pas bloqué;")
Log.create(order_id: 1, exectime: DateTime.new(2000,5,30,4,5,8),  message: "FAIL:: Notifie d'un échec dans l'éxécution;")

Log.create(order_id: 3, exectime: DateTime.new(2000,5,30,4,6,7),  message: "SUCCESS:: Notifie d'un succès;")
Log.create(order_id: 2, exectime: DateTime.new(2000,5,30,4,6,6),  message: "SUCCESS:: Notifie d'un succès;WARNING:: Notifie d'une anomalie;")
Log.create(order_id: 5, exectime: DateTime.new(2000,5,30,4,6,8),  message: "FAIL:: Notifie d'un échec dans l'éxécution;")
=end


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
