module PagesHelper
	def prefix_of_log(myLog)
		
		if myLog.include? "WARNING::"
			return "WARNING"
		elsif myLog.include? "SUCCESS::"
			return "SUCCESS"
		elsif myLog.include? "FAIL::"
			return "FAIL"
		end
	end

	def unprefix_this_log (myLog)
		return myLog
		.gsub("SUCCESS::","").to_s
		.gsub("SUCCESS:: ","").to_s
		.gsub("WARNING::","").to_s
		.gsub("WARNING:: ","").to_s
		.gsub("FAIL::","").to_s
		.gsub("FAIL:: ","").to_s
	end
end
