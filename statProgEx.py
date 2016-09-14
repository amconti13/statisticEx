import math

numbers = input("Enter the values to analyze: ")
numlist = numbers.split() #by default is a space

#numlist is a list of strings, must convert each item to an int
intlist = []
for s in numlist :
    intlist.append(int(s))

#average
sum = 0
for i in intlist :
    sum += i

N = len(intlist)
average = sum / N
print("The average value is", average)

#standard deviation
sum = 0
for i in intlist :
    sum += (i - average) ** 2

stddev = math.sqrt(sum / N)
print("The standard deviation is ", stddev)

#median
intlist.sort()
index = N // 2
median = intlist[index]
print("The median is ", median)

index = 0
maxmode = 0
modelist = []

while index < N:
    c = intlist.count( intlist[index] )
    if c > maxmode :
        maxmode = c
        modelist = [ intlist[index] ]
    elif c == maxmode :
        modelist.append( intlist[index] )

    index += c

print("The mode values that occured" , maxmode, "times are: ", modelist)