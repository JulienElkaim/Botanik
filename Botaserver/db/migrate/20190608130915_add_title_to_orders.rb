class AddTitleToOrders < ActiveRecord::Migration[5.2]
  def change
    add_column :orders, :title, :string
  end
end
