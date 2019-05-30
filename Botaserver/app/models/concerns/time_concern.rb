module TimeConcern
  extend ActiveSupport::Concern

  class_methods do
    def secondConverter(args)
     
	pattern = /^(?<time_value>\w+) (?<time_scale>\w+)$/
	parse_time = args.match(pattern)
	coef = parse_time[:time_value].to_i
	scale = parse_time[:time_scale]
	case scale 
		when /minute/
			scale = 1*60
		when /heure/, /hour/
			scale = 1*60*60
		when /jour/, /day/
			scale = 1*60*60*24
		when /semaine/, /week/
			scale = 1*60*60*24*7
		else
			scale = 1
	end
	
	return coef * scale  
    end

    def another_complicated_method(args)
    	#Something more
    end
  end
end