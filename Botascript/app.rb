require 'time'
require 'selenium-webdriver'
require 'open-uri'


# Gestion des active record cote script !
require_relative "database/connexion"

# p Order.all.size
# p Order.first.alive
# p Order.all.to_a.select(&:alive?)

# 1 Find orders alive :
alive_orders = Order.all.where.not(alive: false)

# 1 Find Orders to exec :
