class CreateOrders < ActiveRecord::Migration[5.2]
  def change
    create_table :orders do |t|
      t.references :user, foreign_key: true
      t.references :network, foreign_key: true
      t.string :intervalle
      t.datetime :exectime
      t.datetime :endtime
      t.string :order_tag
      t.string :order_args

      t.timestamps
    end
  end
end
