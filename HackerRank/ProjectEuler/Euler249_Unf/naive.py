import fileinput

k = 0
n = []
#reading input
foundK = False
for line in fileinput.input():
    if not foundK:
        k = int(line.rstrip())
        foundK = True
    else:
        n = [int(x) for x in line.rstrip().split(' ')]
    pass

max = 0
for i in n:
    if max < i:
        max = i

# bad non-segmented sieve of erat:
primeCandidates = [True for x in range(3,(max)**2+1,2)]
primes = [2]
primeGaps = []
gapSize = 1
for p in range(len(primeCandidates)):
    if(primeCandidates[p]):
        primeGaps.append(gapSize)
        gapSize = 0
        primes.append((2*p+3))
        multiple = (2*p+3)**2
        while(multiple <= (max)**2+1):
            primeCandidates[(multiple-3)//2] = False
            multiple += 2*(2*p+3)
    gapSize += 2
        
print(primes)
#print(primeGaps)

answers = []
# recursive brute force implementation:
def findSubSet(n, primes, primeSet, total=0, curr=0):
    count = 0
    if(curr >= len(primes)):
        return 0
    #print(curr)
    #total += primes[curr]
    tempTotal = total
    for i in range(curr,len(primes)):
        if(primes[i] > max):
            return count
        count += findSubSet(n, primes, primeSet, tempTotal, i+1)
        tempTotal += primes[i]
        if(tempTotal in primeSet):
            print(tempTotal)
            print(curr)
            print(i)
            count += 1
        if(tempTotal < n):
            count += findSubSet(n, primes, primeSet, tempTotal, i+1)
    return count


print(findSubSet(max, primes, set(primes)))       
