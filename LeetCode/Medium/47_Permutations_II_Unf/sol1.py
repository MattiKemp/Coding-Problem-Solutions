# Optimial runtime bad space complexity solution:
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numDict = {}
        for i in nums:
            if numDict.get(i)==None:
                numDict[i] = 1
            else:
                numDict[i] += 1
        queue = deque()
        for i in numDict.keys():
            queue.append([{i:1},i])
        perms = []
        while(len(queue)>0):
            popped = queue.pop()
            if len(popped)-1 == len(nums):
                perms.append(popped[1:])
            else:
                for i in numDict.keys():
                    if popped[0].get(i)!=None:
                        if popped[0][i]<numDict[i]:
                            new = popped[:]
                            new[0] = dict(popped[0])
                            new[0][i] += 1
                            new.append(i)
                            queue.append(new)
                    else:
                        new = popped[:]
                        new[0] = dict(popped[0])
                        new[0][i] = 1
                        new.append(i)
                        queue.append(new)
        return perms




