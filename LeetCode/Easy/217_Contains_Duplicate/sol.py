class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSet = set()
        for i in nums:
            if i in numSet:
                return True
            else:
                numSet.add(i)
        return False
