class ModifyLogins < ActiveRecord::Migration[5.2]
  def change
  	drop_table :logins
  	
  	#create_table :logins, {:id => false} do |t|
	#	t.references :user, foreign_key: true
	#	t.references :network, foreign_key: true
	  #	t.string :network_login
	 # 	t.string :network_password
	#end
	#execute "ALTER TABLE logins ADD PRIMARY KEY (user_);"
	execute "CREATE TABLE logins (
  user_id INTEGER NOT NULL ,
  network_id INTEGER NOT NULL,
  network_login TEXT NOT NULL,
  network_password TEXT NOT NULL,
  PRIMARY KEY ( network_id, user_id)
);"
  end
end
