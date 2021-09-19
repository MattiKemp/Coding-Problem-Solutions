class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        comb = []
        queue = deque()
        queue.append([target,0])
        while(len(queue)>0):
            popped = queue.pop()
            if popped[0] == 0:
                comb.append(popped[2:])
                continue
            for i in range(popped[1],len(candidates)):
                if popped[0]-candidates[i] >= 0:
                    new = popped[:]
                    new.append(candidates[i])
                    new[0] -= candidates[i]
                    new[1] = i
                    queue.append(new)
        return comb


