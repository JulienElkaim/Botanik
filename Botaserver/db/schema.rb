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

ActiveRecord::Schema.define(version: 2019_06_08_130915) do

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

  create_table "logs", force: :cascade do |t|
    t.integer "order_id"
    t.datetime "exectime"
    t.string "message"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["order_id"], name: "index_logs_on_order_id"
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
    t.integer "intervalle", default: 0
    t.datetime "exectime"
    t.datetime "endtime"
    t.string "order_tag"
    t.string "order_args"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.boolean "alive", default: true
    t.string "title"
    t.index ["network_id"], name: "index_orders_on_network_id"
    t.index ["user_id"], name: "index_orders_on_user_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "username"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
    t.index ["username"], name: "index_users_on_username", unique: true
  end

end
