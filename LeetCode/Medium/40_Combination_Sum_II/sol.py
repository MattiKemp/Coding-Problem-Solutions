class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        comb = []
        queue = deque()
        queue.append([target,-1])
        while(len(queue)>0):
            popped = queue.pop()
            if popped[0] == 0:
                comb.append(popped[2:])
                continue
            for i in range(popped[1]+1,len(candidates)):
                if popped[0]-candidates[i] >= 0:
                    if candidates[i] != candidates[i-1] or i == popped[1]+1 :
                        new = popped[:]
                        new.append(candidates[i])
                        new[0] -= candidates[i]
                        new[1] = i
                        queue.append(new)
                else:
                    break          
        return comb                   
