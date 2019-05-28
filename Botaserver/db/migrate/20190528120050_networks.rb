class Networks < ActiveRecord::Migration[5.2]
	def change
	  	create_table :networks
	  	add_column :networks, :network_name, :string

	  	create_table :logins, {:id => false} do |t|
			t.references :user, foreign_key: true
			t.references :network, foreign_key: true
		  	t.string :network_login
		  	t.string :network_password
		end
		#execute "ALTER TABLE logins ADD PRIMARY KEY (user,network);"
	end
  
end
