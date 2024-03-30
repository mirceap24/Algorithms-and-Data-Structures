# Given the head of a linked list, rotate the list to the right by k places.

class ListNode: 
    def __init__(self, value = 0, next = None):
        self.val = value 
        self.next = next 

    def list_to_linkedlist(self, lst):
        # convert list into linked list 
        if not lst: 
            return None 
        head = ListNode(lst[0])
        current = head 
        for value in lst[1:]:
            current.next = ListNode(value)
            current = current.next 
        return head 
    
    def linkedlist_to_list(self, head):
        lst = []
        current = head 
        while current: 
            lst.append(current.val)
            current = current.next 
        return lst

class Solution: 
    def rotateRight(self, head, k):
        # base cases 
        if not head or not head.next or k == 0: 
            return head 
        
        length = 1 
        current = head 
        while current.next: 
            current = current.next 
            length += 1 
        current.next = head # circular 
    
        steps_to_new_head = length - k % length 
        new_tail = head 
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next 
        new_tail.next = None 

        return new_head
    
# Test cases
list_node = ListNode()
solution = Solution()

# Example 1
linked_list_1 = list_node.list_to_linkedlist([1, 2, 3, 4, 5])
rotated_linked_list_1 = solution.rotateRight(linked_list_1, 2)
result_1 = list_node.linkedlist_to_list(rotated_linked_list_1)
print(result_1)