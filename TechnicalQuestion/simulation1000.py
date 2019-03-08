#runs simulation1 1000 and prints out statistics
import random
import numpy as np
import time


#returns tuple of average cost per day and average cost of minimum
def simulate(N):
	# 1000 days
	# 10 gas stations - each day -1,0,+1
	# start from 1001 to 1010

	# get random permutation from 1001 to 1010
	# index is id, value is actual cost of gas station
	actual = np.random.permutation(N)
	actual = [0] + [actual[x] + 1001 for x in range(len(actual))]

	# holds tuples (cost of gas station the last time I visited it, id)
	record = []

	sumcost = 0
	summin = 0

	for day in range(1,1001):
		if(day <= N):
			# visit all gas stations and add to record
			record.append((actual[day],day))
			sumcost+=actual[day]
			summin+=actual[day]

			if(day == N):
				#finish visiting all gas stations, now sort record
				record.sort()
		else:
			#visit first gas station in record, then update record
			record[0] = (actual[record[0][1]],record[0][1])

			sumcost+=record[0][0]
			summin+=min(actual[1:])

			#move record[0]
			index = 0
			while(index < N-1 and record[index][0] >= record[index+1][0]):
				record[index],record[index+1] = record[index+1],record[index]
				index+=1


		#change prices of gas station
		for x in range(1,len(actual)):
			actual[x] += random.randint(-1,1)

	return sumcost/1000,summin/1000


def simulate1000():
	sumcost = 0
	summin = 0
	for i in range(1000):
		if(i % 100 == 0): print(i)
		sc,sm = simulate(10)
		sumcost += sc
		summin += sm

	print("Average Cost: " + str(sumcost/1000))
	print("Average Minimum Cost: " + str(summin/1000))



if __name__ == "__main__":
	start_time = time.time()
	simulate1000()

	print("Run Time: " + str(time.time()-start_time))
