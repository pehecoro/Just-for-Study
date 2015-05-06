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
"""Exercise 6.14
What happens when the list is already organized? Track the program of listing 6.44, but with a new list L=[1,2,3,4,5]"""
#Nothing, 'While' will stop on 1
X = [1,2,3,4,5]
end = 5
while end > 1:
	swap = False
	x=0
	while x<(end-1):
		if X[x] > X[x+1]:
			swap = True
			temp = X[x]
			X[x] = X[x+1]
			X[x+1] = temp
		x+=1
	if not swap:
		break #1
	end-=1
print("-------\n6.14\n-------\n")
for e in X:
	print(e)
"""Exercise 6.15
What happens when there are two equal values? Track the program of listing 6.44, but with a new list L=[3,3,1,5,4]"""
#They rise together
Z = [3,3,1,5,4]
end = 5
while end > 1:
	swap = False
	x=0
	while x<(end-1):
		if Z[x] > Z[x+1]:
			swap = True
			temp = Z[x]
			Z[x] = Z[x+1]
			Z[x+1] = temp
		x+=1
	if not swap:
		break 
	end-=1
print("-------\n6.15\n-------\n")
for e in Z:
	print(e)
"""Exercise 6.16
Change the program of listing 6.44 for order the list in descending order. P = [1,2,3,4,5] must be order as P=[5,4,3,2,1]"""
P = [1,2,3,4,5]
end = 5
while end > 1:
	swap = False
	x=0
	while x<(end-1):
		if P[x] < P[x+1]: #Changed '>' to '<'
			swap = True
			temp = P[x]
			P[x] = P[x+1]
			P[x+1] = temp
		x+=1
	if not swap:
		break 
	end-=1
print("-------\n6.16\n-------\n")
for e in P:
	print(e)
