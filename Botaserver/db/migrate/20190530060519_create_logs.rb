class CreateLogs < ActiveRecord::Migration[5.2]
  def change
    create_table :logs do |t|
      t.references :order, foreign_key: true
      t.datetime :exectime
      t.string :message

      t.timestamps
    end
  end
end
