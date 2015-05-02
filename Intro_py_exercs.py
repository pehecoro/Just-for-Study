"""Exercise 6.12
Change the program of listing 6.33 in order to print the lowest element"""
L=[1,7,2,4]
minimum = L[0]
for e in L:
	if e < minimum:
		minimum = e
print("Ex6.12 \n-------\n%d\n-------" %minimum)

"""Exercise 6.13
The temperatures list of Mons, in Belgium, was stored in list T = [-10,-8,0,1,2,5,-2,-4].
Do a program that print the lowest and the biggest temperature, as well as average temperature"""

T = [-10,-8,0,1,2,5,-2,-4]
#Equal to any element of list
minimum = L[0]
maximum = L[0] 
average = 0
for e in T:
	if e < minimum:
		minimum = e
	if e > maximum:
		maximum = e
	average += e
average /= len(T)
print("Ex6.13 \n-------\nLowest: %d\nBiggest: %d\nAverage: %d\n-------" %(minimum,maximum,average))