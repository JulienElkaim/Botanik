require 'json'
require_relative 'scrappers/linkedin/linkedin'
require 'time'
# Router trop basique, à améliorer !
# Qui va faire les logs sur l'ordre?!

class Processor
  def initialize(order, browser)
    @order = order
    @browser = browser
    @controller = controller_initializer()
    @logs = {}
  end

  def controller_initializer
    case @order.network.network_name
    when "Linkedin"
      return Linkedin.new(@browser)
    else
      # Ajouter d'autres when pour les prochains réseaux supportés
      return nil
    end
  end

  def proceed(mode="botascript")


    if @controller
      # 1 Lance l'ordre
      @logs = @controller.execute(@order)

      # 2 Finir l'ordre proprement
      current_order_finished

    else
      @logs = {"BUG::": "We don't support #{@order.network.network_name} yet."}
      kill_the_order
      save_logs(@logs)
    end


    # 4 Quitte le browser :
    @browser.quit
  end

  def kill_the_order
    # On ne pourra quoi qu'il arrive rien y faire, donc kill l'ordre
    @order.update(alive: false)
  end

  def current_order_finished
    # 1 Actualiser l'ordre si il a besoin
      #=> Changer exectime
      #=> Changer le statut alive
    next_exectime =  Time.now() + @order.intervalle
    if next_exectime > @order.endtime
      kill_the_order
    else
      @order.update(exectime: next_exectime)
    end

    # 2 Sauver les logs d'execution:
    save_logs((@logs.empty?) ? {"SUCCESS::": "How could it be more perfect?!"} : @logs)

  end

  def save_logs(logs)
    @order.logs.create( exectime: Time.now, message: logs)
  end
end
