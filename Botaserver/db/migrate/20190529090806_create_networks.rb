class CreateNetworks < ActiveRecord::Migration[5.2]
  def change
    create_table :networks do |t|
      t.string :network_name

      t.timestamps
    end
    add_index :networks, :network_name, unique: true
  end
end
