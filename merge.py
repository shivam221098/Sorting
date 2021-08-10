# Python program for implementation of MergeSort 
import random 
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 # Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements 
		R = arr[mid:] # into 2 halves 

		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 

		i = j = k = 0
		
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+= 1
			else: 
				arr[k] = R[j] 
				j+= 1
			k+= 1
		
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+= 1
			k+= 1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+= 1
			k+= 1

# Code to print the list 
def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i], end =" ") 
	print() 

# driver code to test the above code
"""for k in range(1, 20000, 100): 
	arr = [random.randint(1, 10000) for i in range(k * 111)] 
	start = time.time()
	mergeSort(arr) 
	print("Time Taken: ", round(time.time() - start, 6))
	x.append(k * 100)
	y.append(round(time.time() - start, 6))

plt.plot(x, y, marker="o")
plt.xlabel("Size")
plt.ylabel("Time")
plt.show()
"""

x = []
y = []
z = []
fig, axes = plt.subplots()
axes.set_xlim(-2, 100)
axes.set_ylim(-2, 100)
line, = plt.plot(0, 0)


def animate(i):
	x.append(i + 1)
	y.append(i + 1)

	line.set_xdata(x)
	line.set_ydata(y)
	return line,


animation = FuncAnimation(fig, func=animate, frames=np.arange(0, 100, 0.5))
plt.show()

# This code is contributed by Mayank Khanna 
