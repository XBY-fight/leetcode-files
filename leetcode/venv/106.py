#!/usr/bin/python
#-*- coding: utf8 -*-
#根据中序遍历和后序遍历构造二叉树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder :
            return None
        root = TreeNode(postorder.pop())
        inorderIndex=inorder.index(root.val)
        root.right=self.buildTree(inorder[inorderIndex+1:], postorder)
        root.left=self.buildTree(inorder[:inorderIndex], postorder)
        return root