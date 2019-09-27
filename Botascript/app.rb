require 'time'
require 'selenium-webdriver'
require 'open-uri'


# Gestion des active record cote script !

require 'active_record'

ActiveRecord::Base.establish_connection(adapter: 'sqlite3',database: '../Botaserver/db/development.sqlite3')

require_relative '../Botaserver/app/models/application_record.rb'
Dir["../Botaserver/app/models/concerns/*.rb"].each do |file|
  require_relative file
end

Dir["../Botaserver/app/models/*.rb"].each do |file|
  require_relative file unless file.include?("user.rb")
end

class User < ApplicationRecord
  has_many :accounts
  has_many :orders
  has_many :logs, :through => :orders
end

p Order.first
p Order.all.size
