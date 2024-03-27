# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):

    def convertListToBST(left, right):
        # Base case - if the left index exceeds the right, we've covered the subarray
        if left > right:
            return None
        
        # Choose the middle element to ensure height balance
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        
        # Recursively form the BST on the subarray to the left and right
        node.left = convertListToBST(left, mid - 1)
        node.right = convertListToBST(mid + 1, right)
        return node

    # Form the BST using the helper function
    return convertListToBST(0, len(nums) - 1)
