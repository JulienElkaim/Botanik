class AddForeignKeysToLogins < ActiveRecord::Migration[5.2]
  def change
  	drop_table :logins
  	
	execute "CREATE TABLE logins (
  user_id INTEGER NOT NULL ,
  network_id INTEGER NOT NULL,
  network_login TEXT NOT NULL,
  network_password TEXT NOT NULL,
  PRIMARY KEY ( network_id, user_id)
);"
	add_foreign_key :logins, :users
	add_foreign_key :logins, :networks
  end
end
