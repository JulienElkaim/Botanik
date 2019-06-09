class OrdersController < ApplicationController

	def index
		#TO DO : Afficher tous les ordres que je possède
		@orders = current_user.orders.sort{|order| Time.now - order.exectime}

	end

end
