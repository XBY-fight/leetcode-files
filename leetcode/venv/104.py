#!/usr/bin/python
#-*- coding: utf8 -*-
#二叉树的最大深度，递归
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depthtree=0
        maxdepth=self.getMaxDepth(root, depthtree)
        print(maxdepth)

    def getMaxDepth(self, root, depthNow) :
        if root is None :
            return depthNow
        return max(self.getMaxDepth(root.left,depthNow+1), self.getMaxDepth(root.right,depthNow+1))
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(7)
root.right.left.right=TreeNode(6)
solution=Solution()
solution.maxDepth(root)