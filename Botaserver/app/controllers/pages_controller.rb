class PagesController < ApplicationController
	skip_before_action :authenticate_user!, only: :autre
  def dashboard
  	@logs = current_user.logs.sort{|log| log.exectime}.reverse
  	@you = current_user
  end

  def autre
  end
  def orders_history
  	@orders = current_user.orders.where(alive: false).sort_by{|order| order.exectime}
  end
end
