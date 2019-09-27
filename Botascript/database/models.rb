
# 1 Le parent de tous les models
require "#{BOTASERVER_PATH}/app/models/application_record.rb"

# 2 Tous les models facile à importer
Dir["#{BOTASERVER_PATH}/app/models/*.rb"].each do |file|
  # Permet d'éviter devise, inutile ici.
  require file unless file.include?("user.rb")
end



# 3 Les models à redéfinir pour notre usage :
class User < ApplicationRecord
  has_many :accounts
  has_many :orders
  has_many :logs, :through => :orders
end
