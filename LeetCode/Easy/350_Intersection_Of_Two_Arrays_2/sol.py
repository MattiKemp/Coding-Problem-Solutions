class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Answers to follow up:
        # Q: What if the given array is already sorted? How would you optimize your  
        # algorithm?
        # A: if both arrays are sorted than you can just traverse both incrementally
        # like: when nums1[m] > nums2[n] increment n, when nums1[m] == nums2[n] append 
        # to intersect and increment m, when nums1[m] < nums2[n] increment m.
        # Runtime: O(m+n) Space: O(1)
        # Q: What if nums1's size is small compared to nums2's size? Which 
        # algorithm is better? 
        # A: I don't know what is meant by which algorithm, but if they aren't
        # sorted than you would want to have nums1 be the dictionary
        # to minimize space.
        # Q: What if elements of nums2 are stored on disk, and the memory is limited such 
        # that you cannot load all elements into the memory at once?
        # A: Proceed with same algorithm below.
        numsDict1 = {}
        for i in nums1:
            if numsDict1.get(i)==None:
                numsDict1[i] = 1
            else:
                numsDict1[i] += 1
        intersect = []
        for i in nums2:
            if numsDict1.get(i)!=None and numsDict1[i]!=0:
                intersect.append(i)
                numsDict1[i] -= 1
        return intersect
        
