# https://leetcode.com/problems/symmetric-tree/description/

class TreeNode: 
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 
    
def isSymmetric(root):
    def isMirror(t1, t2):
        # if both nodes are None, they are mirrors of each other 
        if not t1 and not t2: 
            return True 
        # if only one of the nodes is None, they are not mirros 
        if not t1 or not t2: 
            return False 
        # two nodes are mirrors if they have the same value and their respective
        # left and right subtrees are also mirrors of each other
        return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)
    1
    return isMirror(root, root)