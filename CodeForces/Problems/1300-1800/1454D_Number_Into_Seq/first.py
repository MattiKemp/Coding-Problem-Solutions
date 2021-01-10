import math
t = int(input())
n = [0] * t
max = 0
while t > 0:
    n[len(n)-t] = int(input())
    if(n[len(n)-t] > max):
        max = n[len(n)-t]
    t-=1

#Sieve of Erat
primes = {k:True for k in range(2,int(math.sqrt(max)+2))} 
pwrs = {1}
for k in range(2,len(primes)+2):
    if(primes[k]==True):
        temp = k*k
        while(temp < len(primes)+2):
            primes[temp] = False
            temp += k

prime = {k for k in primes.keys() if primes[k]==True}
for k in n:
    primeF = {}
    temp = k
    for p in prime:
        while(temp%p==0):
            if(primeF.get(p)):
                primeF[p]+=1
            else:
                primeF[p]=1
            temp/=p
    if(temp != 1):
        primeF[int(temp)] = 1
    if(len(primeF)==0):
        print(1)
        print(k)
    else:
        max = 0
        maxP = 0
        for p in primeF.keys():
            if(primeF[p] > max):
                max = primeF[p]
                maxP = p
        print(max)
        for k in range(max-1):
            print(maxP, end =" ")
        final = maxP
        for p in primeF.keys():
            if(p != maxP):
                for k in range(primeF[p]):
                    final*=p
        print(final)
