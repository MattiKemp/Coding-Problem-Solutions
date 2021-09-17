class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums)
        while(begin < end):
            middle = (begin + end)/2
            if(target > nums[middle]):
                begin = middle+1
            elif(target < nums[middle]):
                end = middle
            else:
                return middle
        # fix whether the binary search ended above or below the insertion point
        return middle + (target>nums[middle])
