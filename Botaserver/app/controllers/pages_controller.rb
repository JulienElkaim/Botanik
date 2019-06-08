class PagesController < ApplicationController
	skip_before_action :authenticate_user!, only: :autre
  def dashboard
  	@logs = current_user.logs.sort{|log| log.exectime}
  end

  def autre
  end
end
