require 'active_record'
require_relative 'const'

# Connexion à la base de données:
ActiveRecord::Base.establish_connection(adapter: 'sqlite3',database: "#{BOTASERVER_PATH}/db/development.sqlite3")

# Importe les Helpers des models
require_relative 'helpers'
# Importe les Models.
require_relative 'models'
