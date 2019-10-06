require 'json'
require_relative 'scrappers/linkedin'
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
      return nil
    end
  end

  def proceed(mode="botascript")

    # 1 Lance l'ordre
    @logs = @controller.execute(@order)
    # 2 Quitte le browser

    # 3 Finir l'ordre
    p "héhéhééé #{@logs}"
    finish_order
      # Pas now, save les reportngs
    # 3 Dit à l'ordre de s'actualiser ????:
      # Pas now
    # 4 Quitte le browser :
    @browser.quit
  end

  def finish_order
    # 1 Actualiser l'ordre si il a besoin
      #=> Changer exectime
      @order.update(exectime: Time.now() + @order.intervalle)

      #=> Changer le statut alive

    # 2 Sauver les logs d'execution:
    save_logs((@logs.empty?) ? {success: "GOOD !"} : @logs)
  end

  def save_logs(logs)
    @order.logs.create( exectime: Time.now, message: logs)
  end
end
