#!/usr/bin/python
#-*- coding: utf8 -*-
#恢复二叉树
import sys
class Solution :
    def recoverTree(self, root) :
        import sys
        self.firstElement = None
        self.secondElement = None
        self.prevElement = None
        self.travers(root)
        temp = self.firstElement.val
        self.firstElement.val = self.secondElement.val
        self.secondElement.val = temp

    def travers(self, node):
        if node == None:
            return
        self.travers(node.left)
        if self.firstElement == None and self.prevElement != None and self.prevElement.val >= node.val:
            self.firstElement = self.prevElement
        if self.firstElement != None and self.prevElement.val >= node.val:
            self.secondElement = node
        self.prevElement = node
        self.travers(node.right)
solution=Solution()
solution.recoverTree(None)
