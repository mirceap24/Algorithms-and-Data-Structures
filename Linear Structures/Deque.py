# Implementation of a double-ended queue ("deque") using a doubly linked list 

"""
Deque 
    - push_right
    - push_left 
    - pop_right 
    - pop_left
    - size
"""

class Node(object):
    def __init__(self, val):
        self.val = val 
        self.next = None
        self.prev = None 


class Deque(object):
    def __init__(self):
        self.size = 0 
        self.head = None
        self.tail = None

    def push_right(self, val):
        n = Node(val)
        if self.size == 0:
            self.tail = n 
        else: 
            self.head.next = n
        n.prev = self.head 
        self.head = n 
        self.size += 1

    def push_left(self, val):
        n = Node(val)
        if self.size == 0:
            self.head = n 
        else: 
            self.tail.prev = n
        n.next = self.tail 
        self.tail = n 
        self.size += 1 

    def pop_right(self):
        """
        TAIL HEAD
        A -> B -> None
       
        TAIL
        HEAD
        A -> NONE
        """
        n = self.head
        if n is None: 
            raise ValueError
        self.head = n.prev
        if self.head:
            self.head.next = None
        else: 
            self.tail = None
        self.size -= 1 
        return n.val
    
    def pop_left(self):
        """
       TAIL  HEAD
        A <- B

        TAIL
        HEAD
        B  <- None
        """
        n = self.tail 
        if n is None: 
            raise ValueError
        self.tail = n.next 
        if self.tail: 
            self.tail.prev = None 
        else: 
            self.head = None
        self.size -= 1 
        return n.val 


if __name__ == '__main__':
    d = Deque()
    val1 = "first"
    val2 = "second"

    # test basic push/pop right (stack semantics)
    assert d.size == 0
    d.push_right(val1)
    assert d.size == 1 
    d.push_right(val2)
    assert d.size == 2 
    assert d.pop_right() is val2 
    assert d.size == 1 
    assert d.pop_right() is val1 
    assert d.size == 0

    # test basic push/pop left (stack semantics on other side)
    d.push_left(val1)
    assert d.size == 1 
    d.push_left(val2)
    assert d.size == 2 
    assert d.pop_left() is val2 
    assert d.size == 1 
    assert d.pop_left() is val1 
    assert d.size == 0

    # test push right, pop left side (queue semantics)
    d.push_right(val1)
    d.push_right(val2)
    assert d.pop_left() is val1 
    assert d.pop_left() is val2
    assert d.size == 0 

    # test push left, pop right side (queue semantics)
    d.push_left(val1)
    d.push_left(val2)
    assert d.pop_right() is val1 
    assert d.pop_right() is val2
    assert d.size == 0 
    print('Tests passed')