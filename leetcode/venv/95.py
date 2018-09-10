#!/usr/bin/python
#-*- coding: utf8 -*-
##不同的二叉搜索树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0 :
            return []
        return self.dfs(1, n-1)

    def dfs(self, start, end) :
        if start == end :
            return None
        result=[]
        for i in range(start, end) :
            for l in self.dfs(start, i) or [None] :
                for r in self.dfs(i+1, end) or [None] :
                    node=TreeNode(i)
                    node.left, node.right=l, r
                    result.append(node)
        return result
solution=Solution()
solution.generateTrees(3)