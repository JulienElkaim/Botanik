class PagesController < ApplicationController
  def home
  	r = User.find(1)
  	puts "lol=========" + r.password_digest
  	user = User.find_by_username(r.username)
  	if user.authenticate("Juju13")
  		puts "OOOKKK"
  	else
  		puts "ARG"
  	end
  end
end
