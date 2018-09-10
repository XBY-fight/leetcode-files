#!/usr/bin/python
#-*- coding: utf8 -*-
##寻找二叉树上是否有等于目标值的路径
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None :
            return []
        pathList=[]
        self.getPath(root, sum1, [], pathList)
        return pathList

    def getPath(self, root, sum1, pathlist, pathList) :
        if root.left == None and root.right == None and sum1 == root.val :
            pathlist.append(root.val)
            pathList.append(pathlist)
        if root.left :
            self.getPath(root.left, sum1-root.val, pathlist+[root.val], pathList)
        if root.right :
            self.getPath(root.right, sum1-root.val, pathlist+[root.val], pathList)
root=TreeNode(5)
root.left=TreeNode(4)
root.right=TreeNode(8)
root.right.left=TreeNode(13)
root.right.right=TreeNode(4)
root.right.right.right=TreeNode(1)
root.right.right.left=TreeNode(5)
root.left.left=TreeNode(11)
root.left.left.left=TreeNode(7)
root.left.left.right=TreeNode(2)
solution=Solution()
output=solution.hasPathSum(root, 22)
print(output)