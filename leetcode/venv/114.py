#!/usr/bin/python
#-*- coding: utf8 -*-
##二叉树展开为链表
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        root2=root
        while root2 :
            if root2.left :
                temp=root2.left
                while temp.right :
                    temp=temp.right
                temp.right=root2.right
                root2.right=root2.left
                root2.left=None
            root2=root2.right