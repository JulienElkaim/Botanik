class AccountsController < ApplicationController

	def index
		@accounts = Account.where(user_id: current_user.id)
	end
	def new
		@account = Account.new
	end

	def edit
		pre_account = Account.find(params[:id]) 
		if pre_account.user_id != current_user.id
			flash[:alert] = "Vous tentez d'accéder à un compte ne vous appartenant pas."
			redirect_to "/accounts"
		end
		@account = (current_user.id == pre_account.user_id) ? pre_account : Account.new
	end

	def create
		tmp_params = account_params
		tmp_params["user_id"] = current_user.id
		
		

		@account = Account.new(tmp_params)
		@account.save

		if !@account.id
			puts "loooooool"
			flash[:alert] = "Vous possédez déjà un compte sur #{Network.find(tmp_params["network_id"]).network_name} !"
			redirect_to "/accounts"
		else
			redirect_to accounts_path
		end
		# Will raise ActiveModel::ForbiddenAttributesError
	end

	def update
		@account = Account.find(params[:id])
		
		if current_user.id != @account.user_id
			flash[:alert] = "Vous ne possédez pas ce compte #{@account.network.network_name}."
			
		else
			@account.update(account_params)
		end
		redirect_to accounts_path
		# Will raise ActiveModel::ForbiddenAttributesError
	end

	def destroy
		@account = Account.find(params[:id])
		if @account.user_id == current_user.id 
			@account.destroy
		else
			flash[:alert] = "Ce compte ne t'appartient pas."
		end

		redirect_to accounts_path
	end

	def account_params
    params.require(:account).permit(:network_login, :network_password, :network_id)
  end
end
