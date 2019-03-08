#simulation #1 - 2/4/19 - runs 1 simulation using basic strategy, prints statistics, and outputs graph
import random
import numpy as np
import time
import matplotlib.pyplot as plt


def simulate(N):
	# 1000 weeks
	# 10 gas stations - each week -1,0,+1
	# start from 1001 to 1010

	# get random permutation from 1001 to 1010
	# index is id, value is actual cost of gas station
	actual = np.random.permutation(N)
	actual = [0] + [actual[x] + 1001 for x in range(len(actual))]

	# holds tuples (cost of gas station the last time I visited it, id)
	record = []

	#holds data to output - tuple of (Cost, Station ID, most optimal cost)
	data = [0]
	for week in range(1,1001):
		if(week <= N):
			# visit all gas stations and add to record
			record.append((actual[week],week))
			data.append((actual[week],week,1000))
			if(week == N):
				#finish visiting all gas stations, now sort record
				record.sort()
		else:
			#visit first gas station in record, then update record
			record[0] = (actual[record[0][1]],record[0][1])
			data.append((record[0][0],record[0][1],min(actual[1:])))

			#move record[0]
			index = 0
			while(index < N-1 and record[index][0] >= record[index+1][0]):
				record[index],record[index+1] = record[index+1],record[index]
				index+=1


		#change prices of gas station
		for x in range(1,len(actual)):
			actual[x] += random.randint(-1,1)

	return data

#prints out data
def outputp(data):
	print("Week\t\tCost\t\tMinimum\t\tStation ID")

	for i in range(1,1001):
		print(str(i) + "\t\t" + str(data[i][0]) + "\t\t" + str(data[i][2]) + "\t\t" + str(data[i][1]))

#graph data using matplotlib
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


	data = simulate(10)

	# print statistics and graph data
	outputp(data)
	graph(data)
