
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# this soltuion just iterates through both trees at the same time since they are copies of each other.
# Once again using dfs implemented with a stack, but since we are looping through both we need two stacks.
# Runtime: O(n), where n is the number of nodes in the tree, memory: O(h), where h is the height of the tree
# but as stated in the other solutions, h could be n as the binary tree is not height balanced.
# all of my solutions can be implemented recursively with the same runtimes and memory usages. 
# See optimized recursive for an example
class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        stackog = deque()
        stackog.append(original)
        stackClone = deque()
        stackClone.append(cloned)
        while(True):
            poppedog = stackog.pop()
            poppedClone = stackClone.pop()
            if(poppedog.left):
                stackog.append(poppedog.left)
                stackClone.append(poppedClone.left)
            if(poppedog.right):
                stackog.append(poppedog.right)
                stackClone.append(poppedClone.right)
            if(poppedog==target):
                return poppedClone

def main():
    print('test')

if __name__ == '__main__':
    main()
