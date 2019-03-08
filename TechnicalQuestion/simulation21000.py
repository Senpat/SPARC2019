#runs simulation1 1000 and prints out statistics
import random
import numpy as np
import time
from math import log
import sys

TOTALSIM = 10000

EXPC = 5.0
LOGBASE = 2



def simulate(N):
	# 1000 days
	# 10 gas stations - each day -1,0,+1
	# start from 1001 to 1010

	# get random permutation from 1001 to 1010
	# index is id, value is actual cost of gas station
	actual = np.random.permutation(N)
	actual = [0] + [actual[x] + 1001 for x in range(len(actual))]

	# holds tuples (cost of gas station the last time I visited it, last time I visited it, id)
	record = []


	sumcost = 0
	summin = 0

	#holds data to output - tuple of (Cost, Station ID, most optimal cost)
	data = [0]
	for day in range(1,1001):
		if(day <= N):
			# visit all gas stations and add to record
			record.append((actual[day],day,day))
			data.append((actual[day],day,1000))
			sumcost+=actual[day]
			summin+=actual[day]
			if(day == N):
				#finish visiting all gas stations, now sort record
				record.sort()
		else:

			#see if it is worth visiting a suboptimal gas station
			found = False
			for i in range(1,N):
				if(log((day-record[i][1])/EXPC,LOGBASE)+1 >= record[i][0]-record[0][0]):
					record[i] = (actual[record[i][2]],day,record[i][2])
					found = True
					break

			#visit first gas station in record, then update record
			if(not found):
				record[0] = (actual[record[0][2]],day,record[0][2])

			#resort record based on the changes
			record.sort()

			#update data
			data.append((record[0][0],record[0][2],min(actual[1:])))

			sumcost+=record[0][0]
			summin+=min(actual[1:])

		#change prices of all gas stations
		for x in range(1,len(actual)):
			actual[x] += random.randint(-1,1)

	return sumcost/1000,summin/1000


def simulate1000():
	print("EXPC: " + str(EXPC))
	sumcost = 0
	summin = 0
	for i in range(TOTALSIM):
		if(i % 100 == 0): print(i)
		sc,sm = simulate(10)
		sumcost += sc
		summin += sm

	print("Average Cost: " + str(sumcost/TOTALSIM))
	print("Average Minimum Cost: " + str(summin/TOTALSIM))



if __name__ == "__main__":
	start_time = time.time()


	if(len(sys.argv)>1):
		EXPC = float(sys.argv[1])


	simulate1000()

	print("Run Time: " + str(time.time()-start_time))
