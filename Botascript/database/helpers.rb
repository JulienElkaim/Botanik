Dir["#{BOTASERVER_PATH}/app/models/concerns/*.rb"].each do |file|
  require file
end
