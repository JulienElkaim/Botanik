module PagesHelper
	def prefix_of_log(myLog)
		
		if myLog.message.include? "WARNING::"
			return "WARNING"
		elsif myLog.message.include? "SUCCESS::"
			return "SUCCESS"
		elsif myLog.message.include? "FAIL::"
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
