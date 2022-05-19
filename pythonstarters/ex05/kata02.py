tool = (3, 30, 2019, 9, 25)

def hoursbro(time):
	print("%02d/%02d/%04d %02s:%02s" % (time[3], time[4], time[2], time[0], time[1]))

hoursbro(tool)