import random 
import matplotlib.pyplot as plt
import numpy as np
lst = list(range(100))
random.shuffle(lst)
tmep = 0 
lst2 = []
plt.ion()
print(lst)

for i in range(len(lst)-1) : 
	for j in range(len(lst)-1) : 
		if lst[j]<lst[j+1] :
			temp=lst[j+1]
			lst[j+1]=lst[j]
			lst[j]=temp
			lst2.append(lst[:])
		else : 
			continue 
x = np.array(lst)
for t in lst2 :
	plt.clf()
	c = np.array(t)
	plt.plot(x, c)
	plt.pause(0.01)
	plt.show()
print(lst)
