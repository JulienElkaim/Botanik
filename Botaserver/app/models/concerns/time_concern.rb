module TimeConcern
  extend ActiveSupport::Concern

  class_methods do


    def secondConverter(args)
    	#Convert string in integer of seconds
        if args.downcase.include?("jamais")
            return 0
        end
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
				scale = 2
		end
	       
		return (coef * scale)

    end


    def integerConverter(arg)
    	#Convert integer of second in string
    	time = arg.round
    	one_minute = 60
    	one_hour = 60 * one_minute
    	one_day = 24 * one_hour
    	one_week = 7 * one_day

    	if time <= 0 
    		return "Jamais"
    	elsif (time % one_week) < time
    		#Plus Grand que une semaine
    		coef = time / one_week
    		time_word = "semaine"
    	elsif (time % one_day) < time
    		#Plus Grand que un jour
    		coef = time / one_day
    		time_word = "jour"
    	elsif (time % one_hour) < time
    		#Plus Grand que une heyre
    		coef = time / one_hour
    		time_word = "heure"
    	elsif (time % one_minute) < time
    		#Plus Grand que une minute
    		coef = time / one_minute
    		time_word = "minute"
    	else
    		#Plus Grand que une seconde
    		coef = time
    		time_word = "seconde"
    	end

    	time_word+= "s" if coef != 1
    	
        puts "======TEST==" + "#{coef} #{time_word}"
    	return "#{coef} #{time_word}"
    	
    end
  end
end