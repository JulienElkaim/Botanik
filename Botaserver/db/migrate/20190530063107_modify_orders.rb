class ModifyOrders < ActiveRecord::Migration[5.2]
  def change
  	change_column :orders, :intervalle, :integer, default: 0
  	add_column :orders, :alive, :boolean, default: true
  end
end
