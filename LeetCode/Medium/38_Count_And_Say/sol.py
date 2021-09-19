class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        current = "1"
        for i in range(n-1):
            next = []
            spot = 0
            currChar = current[0]
            currCount = 0
            for i in range(len(current)):
                if currChar != current[i]:
                    next.append(str(currCount)+currChar)
                    currChar = current[i]
                    currCount = 1
                else:
                    currCount += 1
            next.append(str(currCount)+currChar)
            #print(next)
            current = "".join(next)
        return current
