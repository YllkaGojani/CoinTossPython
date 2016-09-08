import random
import math

countH = 0
countT = 0
for i in range(1, 5001):
	random_num = round(random.random())
	if random_num == 0:
		face = 'tail'
		countT += 1
	else:
		face = 'head'
		countH += 1
	print 'Attempt #',i,': Throwing a coin... It is a',face,'... Got',countH,' heads and',countT,' tails.'		
print 'ending the program,thank you!'