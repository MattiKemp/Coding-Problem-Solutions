# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput

q = 0
nm = []
max = 80

#reading input
for line in fileinput.input():
    if ' ' not in line.rstrip():
        q = int(line.rstrip())
    else:
        nm.append([int(x) for x in line.rstrip().split(' ')])
        if nm[-1][0] > max:
            max = nm[-1][0]
    pass

# you only the need the first 9 factorials since the largest factorial is based on the largest
# digit, which is 9.
# naive factorial calculation:
facts = [1]
fact = 1
for i in range(1,10):
    fact *= i
    facts.append(fact)
print(facts)

gis = [0 for x in range(max)]

foundGis = 0
i = 1
while(foundGis < max):
    total = 0
    tempI = i
    while(tempI > 0):
        total += facts[tempI%10]
        tempI //=10
    sf = 0
    totalTemp = total
    while(totalTemp > 0):
        sf += totalTemp%10
        totalTemp //= 10
    #print('i:' + str(i))
    #print(total)
    #print(sf)
    if sf < max and gis[sf-1]==0:
        gis[sf-1] = i
        foundGis += 1
    if i %100 == 0:
        print(gis)
    i+=1
print(gis)
# come back to this one

