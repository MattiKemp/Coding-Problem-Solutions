class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {nums[x]:x for x in range(len(nums))}
        for i in range(len(nums)):
            if numDict.get(target-nums[i])!=None and numDict[target-nums[i]]!=i:
                return [i, numDict[target-nums[i]]]
        # problem doesn't ask for it but just incase there is no solution
        return [-1, -1]
