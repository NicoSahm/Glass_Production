class packing(object):
	stock_lane1
	stock_lane2
	stock_lane3
	output_lane1
	output_lane2
	output_lane3
	def receive_lane1(amount):
		stock_lane1 += amount
		pass
	def receive_lane2(amount):
		stock_lane2 += amount
		pass
	def receive_lane3(amount):
		stock_lane3 += amount
		pass
	def package_lane1():
		if(stock_lane1 >= 1):
			#Sleep 20s Packaging duration
			stock_lane1 -= 1
			output_lane1 += 1
		pass
	def package_lane2():
		if(stock_lane2 >= 1):
			#Sleep 20s Packaging duration
			stock_lane2 -= 1
			output_lane2 += 1
		pass
	def package_lane3():
		if(stock_lane3 >= 1):
			#Sleep 20s Packaging duration
			stock_lane3 -= 1
			output_lane3 += 1
		pass
	def output():
		return(output_lane1 + output_lane2 + output_lane3)



