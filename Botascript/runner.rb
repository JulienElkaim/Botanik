require 'selenium-webdriver'
require_relative 'treatment/processor'

def run_botascript

  # 1 Find orders to execute
    # => Alive, exec triggered, not processing
  taff = Order.exec_scope()

  # 2 Les marquer IN_PROCESS:
  taff.each do |order|
    order.update(processing: true)
    # Marquer les ordres IN_PROCESS
  end


  # 3 Lance les ordres en parallèle:
  sons = []
  taff.each do |order|
    sons << fork do
      # 3.0.b S'assurer que la db est bien connected :
      preventive_db_reconnection()

      # 3.1 Créer le web browser:
      options = Selenium::WebDriver::Chrome::Options.new
      options.add_argument('--headless')
      browser = Selenium::WebDriver.for :chrome#, options: options

      # 3.2 Passer la main au processor qui va traiter l'ordre:
      processor  = Processor.new(order, browser)
      processor.proceed(mode="testing")
    end
    # Fils mort à partir d'ici....

  end

  # 4 Donner 10 minutes pour finir, sinon kill :
  terminated_sons =[]
  begin
    Timeout.timeout(60*10) do
      sons.size.times {terminated_sons << Process.wait}
    end
  rescue Timeout::Error
    unterminated_sons = sons.select{|son| !terminated_sons.include?(son) }
    unterminated_sons.each do |son|
      Process.kill 9, son
      Process.wait son
      # ENHANCEMENT: Savoir quel ordre les unterminated avaient, et créer le log de la défaite !
    end
  end

  # 5 Enlever le IN PROCESS attribute : "processing"
  taff.each do |order|
    order.update(processing: false)
    # Marquer les ordres NOT_IN_PROCESS
  end

  # 6 Remplir des logs GLOBALES d'exec de Botascript
  # => Botascript a t'il été obligé de tuer ses process fils?
  key = "#{Time.now}"
  value = (unterminated_sons.nil? || unterminated_sons.empty?) ? "Pas d'enfanticide" : "J'ai kill #{unterminated_sons.size} de mes enfants..."
  log = "{\"#{key}\": \"#{value}\"};"
  return log
end
