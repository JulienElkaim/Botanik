class PagesController < ApplicationController
	skip_before_action :authenticate_user!, only: :autre
  def dashboard
  end

  def autre
  end
end
