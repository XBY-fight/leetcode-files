#!/usr/bin/python
#-*- coding: utf8 -*-
# Definition for a binary tree node.
#二叉树中序遍历
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        valList=[]
        self.inorderTraver(root, valList)
        print(valList)

    def inorderTraver(self, node, valList) :
        if node != None :
            self.inorderTraver(node.left, valList)
            valList.append(node.val)
            self.inorderTraver(node.right, valList)

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(7)
root.right.left.right=TreeNode(6)
solution=Solution()
solution.inorderTraversal(root)