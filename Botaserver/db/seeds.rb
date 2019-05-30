# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

#Create Users
# 10.times do |i|

# 	u = User.create(username: "Julien#{i}", password: "Juju#{i}")

# end


# linkedin = Network.new(id: 1, network_name: "Linkedin" )
# linkedin.save

# acc = Account.new(id: 1, user_id: 1, network_id: 1, network_login: "monloginLinkedin", network_password: "monPwdLinkedin" )
# acc.save


#Create order

# Order.create(user_id: 1, network_id: 1, intervalle: 60*60*24*7*3, exectime: DateTime.new(2001,2,3,4,5,6), endtime: DateTime.new(2001,2,3,4,5,6), order_tag: "tag order", order_args: "plein darguments")
# p (Order.first.user.orders)

#Users created (id, username, password)
#Networks created (id, network_name)

#accounts created (id, user_id, network_id, network_login, network_password)
	#network_id et user_id referencés comme des FK : OK !
	#

#orders created (id, user_id, network_id, intervalle, exectime, endtime, order_tag, order_args)

#logs created (id, order_id, exectime, message)

# MAKE SOME EXEC STUFF
ordre = Order.first
puts ordre.user.accounts.where(network: ordre.network).first.network_password
puts ordre.network.network_name