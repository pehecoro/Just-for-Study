"""Exercise 6.12
Change the program of listing 6.33 in order to print the lowest element"""
def first():
	L=[1,7,2,4]
	minimum = L[0]
	for e in L:
		if e < minimum:
			minimum = e
	print("Ex6.12 \n-------\n%d\n-------" %minimum)

"""Exercise 6.13
The temperatures list of Mons, in Belgium, was stored in list T = [-10,-8,0,1,2,5,-2,-4].
Do a program that print the lowest and the biggest temperature, as well as average temperature"""
def second():
	T = [-10,-8,0,1,2,5,-2,-4]
	#Equal to any element of list
	minimum = T[0]
	maximum = T[0] 
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
def third():
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
def fourth():
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
def fifth():
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
"""Exercise 6.17
Change the program of listing 6.53 in order to request the user for the product and the quantity sold. Verify if the product name typed exists
in dictionary, and only then make the low in stock"""
def sixth():
	stock = { "pineapple": [1000,1.30],
			  "apple": [200,2.5],
			  "orange": [100,1.7],
			  "banana": [300,2.2],
	}
	sale = []
	total = 0
	product = ""
	quantity = 99999
	while(True):
		while(product != "end"):
			product = input("What product do you'll sell?(leave 'end')")
			if(product in stock):
				break
			else:
				print("This product doesn't exists.")
		if(product == "end"):
			break
		while(stock[product][0] < quantity):
			quantity = int(input("How much?"))
			if stock[product][0] < quantity:
				print("Unfortunately, we don't have this quantity.")
		sale.extend([[product,quantity]])
	for operation in sale:
		product, quantity = operation
		price = stock[product][1]
		cost = price * quantity
		print("%11s: %3d * %6.2f = %f" %
			  (product,quantity,price,cost))
		stock[product][0] -= quantity
		total += cost
	print("Total cost: %21.2f\n" %total)
	print("Stock:\n")
	for key,data in stock.items():
		print("Description: ", key)
		print("Quantity: ", data[0])
		print("Price: %6.2f" %data[1])
options = { 2: first,
			3: second,
			4: third,
			5: fourth,
			6: fifth,
			7: sixth,
}
while(True):
	num = int(input("Exercise 6,1?(2<=x<=7):"))
	options[num]()