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

ActiveRecord::Schema.define(version: 2019_05_29_100825) do

  create_table "accounts", force: :cascade do |t|
    t.integer "user_id"
    t.integer "network_id"
    t.string "network_login"
    t.string "network_password"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["network_id"], name: "index_accounts_on_network_id"
    t.index ["user_id"], name: "index_accounts_on_user_id"
  end

  create_table "networks", force: :cascade do |t|
    t.string "network_name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["network_name"], name: "index_networks_on_network_name", unique: true
  end

  create_table "orders", force: :cascade do |t|
    t.integer "user_id"
    t.integer "network_id"
    t.string "intervalle"
    t.datetime "exectime"
    t.datetime "endtime"
    t.string "order_tag"
    t.string "order_args"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["network_id"], name: "index_orders_on_network_id"
    t.index ["user_id"], name: "index_orders_on_user_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "username"
    t.string "password_digest"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["username"], name: "index_users_on_username", unique: true
  end

end
