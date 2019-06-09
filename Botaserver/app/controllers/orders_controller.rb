class OrdersController < ApplicationController

	def index
		#TO DO : Afficher tous les ordres que je possède
		@orders = current_user.orders.sort_by{|order| order.exectime}

	end

	def new
		@order = Order.new
	end

	def create
		tmp_params = order_params
		tmp_params["user_id"] = current_user.id
		tmp_params["order_args"] = "{}" if tmp_params["order_args"] == ""
		

		@order = Order.new(tmp_params)
		@order.save

		if !@order.id
	
			flash[:alert] = "Vous essayez d'usurper notre système d'enregistrement d'ordre!"
			redirect_to "/orders"
		else
			redirect_to orders_path
		end
		# Will raise ActiveModel::ForbiddenAttributesError
	end






	def edit
		session[:referrer] = request.referrer
		@order = Order.find(params[:id]) 
		if @order.user_id != current_user.id
			flash[:alert] = "Vous ne pouvez pas modifier un ordre ne vous appartenant pas."
			redirect_to "/orders"
		end

		
	end


	def update
		referrer  = session.delete(:referrer)
		@order = Order.find(params[:id])
		pre_params = order_params
		pre_params[:intervalle] = Order.convertTime(pre_params[:intervalle])
		
		if current_user.id != @order.user_id
			flash[:alert] = " L'ordre #{@order.title} ne vous appartient pas."
		else
			@order.update(pre_params)
		end
		redirect_to orders_path
		# Will raise ActiveModel::ForbiddenAttributesError
	end


	def show
	end

	# def create
	# 	tmp_params = account_params
	# 	tmp_params["user_id"] = current_user.id
		
		

	# 	@account = Account.new(tmp_params)
	# 	@account.save

	# 	if !@account.id
	
	# 		flash[:alert] = "Vous possédez déjà un compte sur #{Network.find(tmp_params["network_id"]).network_name} !"
	# 		redirect_to "/accounts"
	# 	else
	# 		redirect_to accounts_path
	# 	end
	# 	# Will raise ActiveModel::ForbiddenAttributesError
	# end

	# def update
	# 	@account = Account.find(params[:id])
		
	# 	if current_user.id != @account.user_id
	# 		flash[:alert] = "Vous ne possédez pas ce compte #{@account.network.network_name}."
			
	# 	else
	# 		@account.update(account_params)
	# 	end
	# 	redirect_to accounts_path
	# 	# Will raise ActiveModel::ForbiddenAttributesError
	# end

	def order_params
    	params.require(:order).permit(:title, :network_id, :intervalle, :exectime, :endtime, :order_tag, :order_args)
  	end

end
