class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsDict = {}
        for i in range(len(nums)):
            if numsDict.get(nums[i])==None:
                numsDict[nums[i]] = {i}
            else:
                numsDict[nums[i]].add(i)
        sumDict = {}
        for i in range(len(nums)):
            for j in numsDict.keys():
                sum = nums[i] + j
                if i not in numsDict[j] or len(numsDict[j])>1:
                    if sumDict.get(sum)==None:
                        sumDict[sum] = {nums[i]}
                    else:
                        if j not in sumDict[sum]:
                            sumDict[sum].add(nums[i])
        print(sumDict)
        triplets = []
        for i in range(len(nums)):
            if sumDict.get(-nums[i])!=None:
                if nums[i] not in sumDict[-nums[i]] or len(numsDict[nums[i]])>1:
                    while(len(sumDict[-nums[i]])>0):
                        first = sumDict[-nums[i]].pop()
                        second = None
                        if(first*2 == -nums[i]):
                            if first != nums[i] or len(numsDict[nums[i]])>2:
                                triplets.append([nums[i], first, first])
                        else:
                            #sumDict[-nums[i]].remove(-nums[i]-first)
                            second = -nums[i]-first
                            triplets.append([nums[i], first, second])
                        secondSum = nums[i]+first
                        if nums[i] in sumDict[secondSum]:
                            sumDict[secondSum].remove(nums[i])
                            if first in sumDict[secondSum]:
                                sumDict[secondSum].remove(first)
                            if len(sumDict[secondSum])==0:
                                sumDict.pop(secondSum, None)
                        if second and nums[i] in sumDict[nums[i]+second]:
                            sumDict[nums[i]+second].remove(nums[i])
                            if second in sumDict[nums[i]+second]:
                                sumDict[nums[i]+second].remove(second)
                            if len(sumDict[nums[i]+second])==0:
                                sumDict.pop(nums[i]+second, None)
                    sumDict.pop(-nums[i], None)
        print(triplets)
        return triplets
                        
                        
                    
            
