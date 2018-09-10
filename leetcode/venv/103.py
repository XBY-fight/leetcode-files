#!/usr/bin/python
#-*- coding: utf8 -*-
#二叉树锯齿层序遍历
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root :
            return []
        res, temp, stack, flag=[], [], [root], 1
        while stack :
            for i in range(len(stack)) :
                node=stack.pop()
                temp+=[node.val]
                if node.left : stack=[node.left]+stack
                if node.right : stack=[node.right]+stack
            res+=[temp[::flag]]
            temp=[]
            flag*=-1
        return res

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(7)
root.right.left.right=TreeNode(6)
solution=Solution()
output=solution.zigzagLevelOrder(root)
print(output)