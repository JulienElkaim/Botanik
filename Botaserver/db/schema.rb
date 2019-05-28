# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2019_05_28_132858) do

  create_table "logins", primary_key: ["network_id", "user_id"], force: :cascade do |t|
    t.integer "user_id", null: false
    t.integer "network_id", null: false
    t.text "network_login", null: false
    t.text "network_password", null: false
  end

  create_table "networks", force: :cascade do |t|
    t.string "network_name"
  end

  create_table "orders", force: :cascade do |t|
    t.integer "intervalle"
    t.datetime "exec_time"
    t.datetime "Final_time"
    t.string "order_tag"
    t.string "order_args"
    t.integer "user_id"
    t.integer "network_id"
    t.index ["network_id"], name: "index_orders_on_network_id"
    t.index ["user_id"], name: "index_orders_on_user_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "username"
    t.string "password_digest"
  end

end
