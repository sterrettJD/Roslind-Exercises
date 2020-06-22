ints = list(map(int,input('Please enter the numbers of AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, and aa-aa couples (in that order, separated by spaces).\n').split()))
domoff, i = 0, 0

while i < 5:
    if i < 3:
        domoff += ints[i] * 2
    elif i == 3:
        domoff += ints[i] * 1.5
    elif i == 4:
        domoff += ints[i] * 1
    i += 1
    
print('It is expected that there will be {} offspring displaying the dominant phenotype, under the assumption that every couple has exactly two offspring.'.format(domoff))
