class CreateOrdersTable < ActiveRecord::Migration[5.2]
  def change
    create_table :orders_tables do |t|
    	t.integer      :intervalle
    	t.datetime      :exec_time
    	t.datetime      :Final_time
    	t.string      :order_tag
    	t.string      :order_args
    	t.references  :user, foreign_key: true
    	t.references  :network, foreign_key: true
    end
  end
end
