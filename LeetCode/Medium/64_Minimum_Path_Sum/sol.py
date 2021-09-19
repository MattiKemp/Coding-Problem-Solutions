# if you are allowed to modify the input
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid[0])-2,-1,-1):
            grid[-1][i] += grid[-1][i+1]
        for i in range(len(grid)-2,-1,-1):
            grid[i][-1] += grid[i+1][-1]
        for spotY in range(len(grid)-2,-1,-1):
            for spotX in range(len(grid[0])-2,-1,-1):
                grid[spotY][spotX] += min(grid[spotY][spotX+1],grid[spotY+1][spotX])
        return grid[0][0]
