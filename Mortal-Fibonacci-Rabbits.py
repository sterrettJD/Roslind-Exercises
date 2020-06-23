#Given: Positive integers n≤100 and m≤20. There is 1 pair of "newborn" rabbits in the first month.
#
#Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
#


n = int(input('What is the time span (in months)?\n'))
d = int(input('How long does each rabbit live (in months)?\n'))
month = 1
rab = [0,0,1]
while month < n:
    if month == 1:
        rab.append(1)
        month += 1
    elif month < d:
        rab.append(rab[-1] + rab[-2])
        month += 1
    elif month == d:
        rab.append(rab[-1]+rab[-2]-1)
        month +=1
    else:
        rab.append(rab[-1] + (rab[-2] - rab[-1*d]) + (rab[d*-1]-rab[(d*-1)-1]))
        month += 1
        
print('There will be {} rabbits after {} months.'.format(rab[-1],n))
