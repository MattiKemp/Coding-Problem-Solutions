# if we are allowed to modify the input
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root, l):
            if root:
                if root.left:
                    helper(root.left, l)
                l.append(root.val)
                if root.right:
                    helper(root.right,l)
        l = []
        helper(root, l)
        return l

# otherwise
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root):
            if root:
                l = [root.val]
                if root.left:
                    l = helper(root.left) + l
                if root.right:
                    l += helper(root.right)
                return l
        return helper(root)
