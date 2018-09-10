# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.numlist=[]
        self.preOrderTraverse(root)
        print(self.numlist)
        minnumi=self.numlist.index(min(self.numlist))
        tempnum=self.numlist[0]
        self.numlist[0]=self.numlist[minnumi]
        self.numlist[minnumi]=tempnum
        print(self.numlist)
        root2=nodetemp=TreeNode(self.numlist[0])
        for nodenum in self.numlist[1::] :
            nodetemp.right=TreeNode(nodenum)
            nodetemp=nodetemp.right
        print(root2.right.right.right.val)

    def preOrderTraverse(self, node) :
        if node == None :
            return
        self.preOrderTraverse(node.left)
        self.numlist.append(node.val)
        self.preOrderTraverse(node.right)


root=TreeNode(5)
root.left=TreeNode(3)
root.right=TreeNode(6)
root.left.left=TreeNode(2)
root.left.left.left=TreeNode(10)
root.left.right=TreeNode(4)
root.right.right=TreeNode(8)
root.right.right.right=TreeNode(9)
root.right.right.left=TreeNode(7)
solution=Solution()
solution.increasingBST(root)