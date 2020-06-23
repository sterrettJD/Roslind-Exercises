#The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.
#
#Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#
#Return: The protein string encoded by s.


with open('aalist.txt') as aalist:
    aas = aalist.read().split()
daas = dict(zip(aas[::2],aas[1::2]))

with open(input('What is the RNA file? (.txt required, must be in the same directory) \n')) as file:
    rna = file.read().strip()
    
aaseq = []

for i in range(0,len(rna),3):
    aaseq.append(daas[rna[i:i+3]])
protein = ''.join(aaseq).replace('Stop','')
print('\n' + protein)
