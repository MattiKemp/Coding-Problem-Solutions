class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# similiar runtime and memory usage as naive.py implementation. However, this version uses
# the property of a dfs stack implementation to get the path from the stack itself.
# If implemented in a certain way the stack will have the path stored in it. This can be 
# done if we only remove nodes from the stack that have been visited more than once.
# this will keep nodes that are on the path to node on the top of stack and nodes that
# haven't been visited yet. We can then recover the path by keeping track how many times a node
# has been visited using the second element in our stack items: False if never visited and True if visited
# once. Nodes that have never been visited can't be in the path to the target node as they weren't involved
# in finding the final node.
class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        stack = deque()
        stack.append([original,False, False])
        while(True):
            popped = stack.pop()
            if(not popped[1]):
                popped[1] = True
                stack.append(popped)
                if(popped[0].left):
                    stack.append([popped[0].left,False, False])
                if(popped[0].right):
                    stack.append([popped[0].right,False, True])
            if(popped[0]==target):
                break
        tempRoot = cloned
        stack.popleft()
        while(len(stack) > 0):
            popped = stack.popleft()
            if(popped[1]):
                if(popped[2]):
                    tempRoot = tempRoot.right
                else:
                    tempRoot = tempRoot.left
        return tempRoot
        

def main():
    print('test')

if __name__ == '__main__':
    main()
