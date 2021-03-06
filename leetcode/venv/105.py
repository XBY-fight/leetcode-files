#!/usr/bin/python
#-*- coding: utf8 -*-
#根据前序遍历和中序遍历构造二叉树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder :
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left=self.buildTree(preorder, inorder[0:ind])
            root.right=self.buildTree(preorder, inorder[ind+1:])
            return root