# require 'time'
# require 'selenium-webdriver'
# require 'open-uri'


def run_botascript

  # 1 Find orders to execute
  taff = Order.exec_scope()

  # 2 Les marquer IN_PROCESS:
  taff.each do |order|
    # Marquer les ordres IN_PROCESS
  end

  # 3 Lance les ordres en parallèle:
  sons = []
  taff.each do |order|
    sons << fork do
      preventive_db_reconnection()
      p "I am the son #{Process.pid}. I do stuff on order n° #{order.id}"

      # STUFF TO DO HERE !
      # STUFF TO DO HERE !
      sleep(15) #Simulate big stuff
      # STUFF TO DO HERE !
      # STUFF TO DO HERE !
    end
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

  # 5 FACULTATIF : Remplir des logs d'exec de Botascript
    # Ces logs servent à rendre compte facilement du nombre de fois
    # Ou le Botascript a du buter ses enfants et
    # les ordres liés à ces enfants
    # => Pour l'instant logs débiles ci dessous:
  key = "#{Time.now}"
  value = (unterminated_sons.nil? || unterminated_sons.empty?) ? "Pas d'enfanticide" : "J'ai kill #{unterminated_sons.size} de mes enfants..."
  log = "{\"#{key}\": \"#{value}\"};"
  return log
end
