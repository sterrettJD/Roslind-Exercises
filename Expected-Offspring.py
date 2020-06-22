#Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, 
#the six given integers represent the number of couples having the following genotypes:
#
#AA-AA
#AA-Aa
#AA-aa
#Aa-Aa
#Aa-aa
#aa-aa
#Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.



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
