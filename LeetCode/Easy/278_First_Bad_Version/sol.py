class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # essentially use a numerical analysis method, pretty sure it is 
        # called the babylonian method or something. Which is pretty much a binary search
        begin = 0
        end = n
        while(begin < end):
            middle = (begin+end)/2
            if(isBadVersion(middle)):
                end = middle
            else:
                begin = middle+1
        return middle+(not isBadVersion(middle))
