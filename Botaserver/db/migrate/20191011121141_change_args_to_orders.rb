class ChangeArgsToOrders < ActiveRecord::Migration[5.2]
  def change
    change_column :orders, :order_args, :jsonb
  end
end
