#based off of simulation2.py
#graphs data
#supports up to 1 command line argument (the constant value for determining if a suboptimal gas station is worth investigating)


import random
import numpy as np
import time
from math import log
import sys
import matplotlib.pyplot as plt

#default constant is 0.0025
EXPC = 0.0025

def simulate(N):
	print("EXPC: " + str(EXPC))
	# 1000 weeks
	# 10 gas stations - each weej -1,0, or +1
	# start from 1001 to 1010

	# get random permutation from 1001 to 1010
	# index is id, value is actual cost of gas station
	actual = np.random.permutation(N)
	actual = [10000] + [actual[x] + 1001 for x in range(len(actual))]

	# holds tuples (cost of gas station the last time I visited it, last time I visited it, id)
	record = []

	#holds data to output - tuple of (Cost, Station ID, most optimal cost)
	data = [0]
	for week in range(1,1001):

		if(week <= N):
			# visit all gas stations and add to record
			record.append((actual[week],week,week))
			data.append((actual[week],week,1000))
			if(week == N):
				#finish visiting all gas stations, now sort record
				record.sort()
		else:


			#see if it is worth visiting a suboptimal gas station
			found = False
			for i in range(1,N):
				if(log((week-record[i][1])/EXPC,2)+1 >= record[i][0]-record[0][0]):
					record[i] = (actual[record[i][2]],week,record[i][2])
					data.append((record[i][0],record[i][2],min(actual[1:])))

					found = True
					break

			#visit first gas station in record, then update record
			if(not found):
				record[0] = (actual[record[0][2]],week,record[0][2])
				data.append((record[0][0],record[0][2],min(actual[1:])))

			#resort record based on the changes
			record.sort()


		#change prices of all gas stations
		for x in range(1,len(actual)):
			actual[x] += random.randint(-1,1)


	return data

#prints out data
def outputp(data):
	print("Week\t\tCost\t\tMinimum\t\tStation ID")

	for i in range(1,1001):
		print(str(i) + "\t\t" + str(data[i][0]) + "\t\t" + str(data[i][2]) + "\t\t" + str(data[i][1]))

def graph(data):
	weeks = []
	costs = []
	minimum = []
	for i in range(1,1001):
		weeks.append(i)
		costs.append(data[i][0])
		minimum.append(data[i][2])

	plt.plot(weeks, costs, color='blue')
	plt.plot(weeks, minimum, color='red')
	plt.xlabel('Weeks')
	plt.ylabel('Dollars')
	plt.title('simulation2')
	plt.gca().set_ylim([900,1025])
	plt.show()


if __name__ == "__main__":
	print()
	random.seed()

	if(len(sys.argv)>1):
		EXPC = float(sys.argv[1])

	data = simulate(10)

	# print statistics and graph data
	outputp(data)
	graph(data)
