#!/usr/bin/python
#-*- coding: utf8 -*-
##二叉树中的最大路径和
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum=float('-inf')
        self.findMax(root)
        return self.maxSum

    def findMax(self, p):
        if p is None: return 0
        left = self.findMax(p.left)
        right = self.findMax(p.right)
        self.maxSum = max(p.val + left + right, self.maxSum)
        ret = p.val + max(left, right)
        return ret if ret > 0 else 0
root=TreeNode(-10)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
solution=Solution()
output=solution.maxPathSum(root)
print(output)