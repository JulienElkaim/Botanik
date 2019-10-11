# ==========================
# Simule un fils qui éxécute un ordre
# ==========================

require_relative "database/connexion"
require_relative 'treatment/processor'
connect_db(); #First time !

victor = User.first
sample_order = Order.new(
  user: victor,
  title: "Every 4 minutes add 10 pers",
  network_id: 1,
  intervalle: Order.convertTime("4 minutes"),
  exectime: Time.now.utc.change(usec: 0),
  endtime: (Time.now.utc + Order.convertTime("1 semaines")).change(usec: 0),
  order_tag: "ADD",
  order_args: {until: 5}
  )


# p sample_order.network

# 1 Créer le web browser:
options = Selenium::WebDriver::Chrome::Options.new
options.add_argument('--headless')
browser = Selenium::WebDriver.for :chrome#, options: options

# 2 Passer la main au processor qui va traiter l'ordre:
processor  = Processor.new(sample_order, browser)
processor.proceed(mode = "crash")


# NEXT STEP:

# Dans le add de linkedin:
# créer la procédure pour add des gens !
# NEXT ? Faire d'autres fonctions sur linkedin.
