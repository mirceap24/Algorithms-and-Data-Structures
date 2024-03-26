# https://leetcode.com/problems/single-number/description/

class ListNode: 
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 
    
    def isPalindrome(head):
        # find the middle of the linked list 
        fast = slow = head 
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 

        # reverse the 2nd half of the list 
        prev = None 
        while slow: 
            temp = slow.next 
            slow.next = prev 
            prev = slow 
            slow = temp 
        
        # compare the first half and reversed second half 
        left, right = head, prev 
        while right: 
            if left.val != right.val: 
                return False 
            left = left.next
            right = right.next 
        
        return True 