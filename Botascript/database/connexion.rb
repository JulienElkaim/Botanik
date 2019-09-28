require 'active_record'
require_relative 'const'

# Connexion à la base de données:
def connect_db
  ActiveRecord::Base.establish_connection(adapter: 'sqlite3',database: "#{BOTASERVER_PATH}/db/development.sqlite3")
end


def preventive_db_reconnection
  ActiveRecord::Base.connection.reconnect! if not ActiveRecord::Base.connected?
end


# Importe les Helpers des models
require_relative 'helpers'
# Importe les Models.
require_relative 'models'
