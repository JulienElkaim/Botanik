require_relative "database/connexion"
connect_db(); #First time !
# Connecté à la db grâce à connect_db() appelé dans connexion

require_relative 'runner.rb'


# Doit boucler toutes les minutes, et lancer le runner du Botascript
loop do
  fork do
    preventive_db_reconnection()
    botalogs = run_botascript()
    File.open('logs.txt', 'a') do |archives|
      archives.write("#{botalogs}")
    end
  end
  sleep(60) #Attendre une minute avant de refaire
end

# =============== BEST WORLD ============
# Chaque minute,
# un process se lance pour exec les ordres
# Il tient compte du fait qu'un autre processus
# est déjà en cours, et ne re fait pas un ordre qui a été lent
# Il marque comme IN_PROCESS chaque ordre qu'il s'apprête à lancer
# Il lance chacun des ordres dans des processus fils, l'un à la suite de l'autre
# Si un de ses proc fils met plus de 5 minutes, il le crash.
# ===============:::::::::::============

