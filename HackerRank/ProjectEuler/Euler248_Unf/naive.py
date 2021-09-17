import fileinput

m = []
k = []
#reading input
foundMNQ = False
for line in fileinput.input():
    if not foundMNQ:
        m = [int(x) for x in line.rstrip().split(' ')]
        foundMNQ = True
    else:
        k.append(int(line.rstrip()))
    pass

sqrtVal = int(m[0]**.5)+1
primeCandidates = [True for x in range(3,sqrtVal,2)]
primes = [2]
for p in range(len(primeCandidates)):
    if(primeCandidates[p]):
        primes.append((2*p+3))
        multiple = (2*p+3)**2
        while(multiple <= sqrtVal):
            primeCandidates[(multiple-3)//2] = False
            multiple += 2*(2*p+3)

#print(primes)

totieVal = m[0]
print(totieVal)
print(primes[-1])
totieFacts = []
for i in primes:
    if i > 30030 and totieVal*i % (i-1) == 0:
        totieFacts.append(i)
        totieVal /= (i-1)

print(totieFacts)
