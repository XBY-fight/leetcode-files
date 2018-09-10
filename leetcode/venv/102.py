#!/usr/bin/python
#-*- coding: utf8 -*-
#二叉树层序遍历
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodelist=[root]
        nodelast=root
        nodenumlist=[]
        nodenumlistall=[]
        while nodelist :
            nodenow=nodelist[0]
            nodenumlist.append(nodenow.val)
            if nodenow.left :
                nodelist.append(nodenow.left)
            if nodenow.right :
                nodelist.append(nodenow.right)
            if nodelist and nodenow == nodelast :
                nodelast=nodelist[len(nodelist)-1]
                nodenumlistall.append(nodenumlist)
                nodenumlist=[]
            del nodelist[0]
        print(nodenumlistall)
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(7)
root.right.left.right=TreeNode(6)
solution=Solution()
solution.levelOrder(root)