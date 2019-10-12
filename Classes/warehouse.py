class warehouse(object):
	stock_lane1
	stock_lane2
	stock_lane3
	output = 12
	def receive_lane1(amount):
		stock_lane1 += amount
		pass
	def receive_lane2(amount):
		stock_lane2 += amount
		pass
	def receive_lane3(amount):
		stock_lane3 += amount
		pass
	def transport_lane1(amount):
		if(stock_lane1 >= output):
			#Sleep 5s Transportduration
			stock_lane1 -= output
		return(output)
	def transport_lane2(amount):
		if(stock_lane2 >= output):
			#Sleep 5s Transportduration
			stock_lane2 -= output
		return(output)
	def transport_lane3(amount):
		if(stock_lane3 >= output):
			#Sleep 5s Transportduration
			stock_lane3 -= output
		return(output)




