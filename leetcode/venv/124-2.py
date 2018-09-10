#!/usr/bin/python
#-*- coding: utf8 -*-
##二叉树中的最大路径和
#form leetcode
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
        # 返回该节点的最大路径，最大左路径，最大右路径
        def dfs(root):
            if not root:
                return float("-inf"), 0  # 返回以该节点为根的最大路径和，与单条的路径
            if root:
                lmax, lpath = dfs(root.left)
                rmax, rpath = dfs(root.right)
                m = max(lmax, rmax, lpath + rpath + root.val)
                path = max(lpath + root.val, rpath + root.val, 0)

                return m, path

        m, path = dfs(root)
        return m
root=TreeNode(-10)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
solution=Solution()
output=solution.maxPathSum(root)
print(output)