#!/usr/bin/python
#-*- coding: utf8 -*-
##二叉树将同一层的兄弟节点连接起来
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None :
            return
        root2=root
        while root2.left :
            cur=root2
            while cur :
                cur.left.next=cur.right
                if cur.next :
                    cur.right.next=cur.next.left
                cur=cur.next
            root2=root2.left