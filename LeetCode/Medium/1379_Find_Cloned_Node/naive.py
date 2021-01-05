# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Naive solution to the problem. Since the two trees are clones of each other all we have to do is
# is find the path to the target in the original one and then follow that path in the cloned version.
# We find the target node using dfs implemented with a stack, we keep track of the path taken
# by appending whether we went right (True) or left (False) at each depth. Once the target node is found
# we follow these left and rights stored. In total the dfs worst case runtime is O(n), where n is the number 
# of nodes, and tracing the path runtime is O(h), where h is the height of the target node in the tree.
# However, since it is not a height balanced tree, the height could be O(n). 
# The memory is primarily where this implementation is optimial as we only ever store O(h) elements in the
# stack, and for each element in the stack O(h) items (path data). So the memory usage would be O(h^2).
# However, as described above, the binary tree is not height balanced so the height could be the number 
# of nodes which would mean the worst case memory usage would be O(N^2).
# This solution also satisfies the problems follow up challenge of their being non-unique nodes in the tree.
# This is done by comparing the reference to the target instead of the targets value. This is important
# as it is decently common for regular binary trees to not have unique nodes.
class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        #Stack implemented with a deque, as i've found this is the nicest way to do it in python
        stack = deque()
        stack.append([original,[]])
        path = None
        # dfs 
        while(len(stack) > 0):
            popped = stack.pop()
            if(popped[0]==target):
                path = popped[1]
                break
            if(popped[0].left):
                stack.append([popped[0].left,popped[1]+[False]])
            if(popped[0].right):
                stack.append([popped[0].right,popped[1]+[True]])
        tempRoot = cloned
        # tracing the path to the target in the original tree in the cloned tree.
        for k in path:
            if(k):
                tempRoot = tempRoot.right
            else:
                tempRoot = tempRoot.left
        return tempRoot

def main():
    print('test')
    

if __name__ == '__main__':
    main()
