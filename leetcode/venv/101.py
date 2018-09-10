#!/usr/bin/python
#-*- coding: utf8 -*-
##判断是否是对称二叉树，用递归进行
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left == None and root.right == None :
            return True
        if root.left == None or root.right == None :
            return False
        if root.left.val != root.right.val :
            return False
        if root.left and root.right :
            return self.searchNode(root.left, root.right)

    def searchNode(self, left, right) :
        if left == None and right == None :
            return True
        if left == None and right != None :
            return False
        if left != None and right == None :
            return False
        if left.val != right.val :
            return False
        return self.searchNode(left.left, right.right) and self.searchNode(left.right, right.left)
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.right.right=TreeNode(3)
root.left.right=TreeNode(4)
root.right.left=TreeNode(4)
solution=Solution()
output=solution.isSymmetric(root)
print(output)