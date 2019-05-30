class CreateAccounts < ActiveRecord::Migration[5.2]
  def change
    create_table :accounts do |t|
      t.references :user, foreign_key: true
      t.references :network, foreign_key: true
      t.string :network_login
      t.string :network_password

      t.timestamps
    end
  end
end
