"""
Linked List:
------------
its seperate nodes that are linked to each other
there are two types of linked lists:
1- singly linked list: each node has a value and a pointer to the next node
2- doubly linked list: each node has a value and a pointer to the next node and a pointer to the previous node

we can use linked lists to implement stacks and queues
we can use linked lists to implement graphs and trees
we can use linked lists to implement hash tables
If we use singly linked lists, we can only traverse the list in one direction(head to tail)
If we use doubly linked lists, we can traverse the list in both directions(header to tailer and tailer to header)

"""
#for singly ->

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

firstNode = Node(10)
secondNode = Node(20)
thirdNode = Node(30)

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode
thirdNode.nextNode = None

print(firstNode.value)
print(firstNode.nextNode.value)
print(firstNode.nextNode.nextNode.value)


# #for doubly ->

class doublyNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


firstNode = doublyNode(10)
secondNode = doublyNode(20)
thirdNode = doublyNode(30)

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode
thirdNode.nextNode = None

thirdNode.prev = secondNode
secondNode.prev = firstNode
firstNode.prev = None


print(f"second node's value is: {thirdNode.prev.value} from third's prev")
print(f"first node's value is: {thirdNode.prev.prev.value} from third's double prev")


# #for circular ->

class circularNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
    def insert(self, value):
        if self.next == None:
            self.next = circularNode(value)
            self.next.prev = self
        else:
            self.next.insert(value)
    
"""
append is adding a new node to the end of the list
pop is removing the last node of the list
prepend is adding a new node to the beginning of the list
pop first is removing the first node of the list
access (index) is getting the value of the node at a certain position
access (value) is getting the value of the node with a certain value
remove is removing the node with a certain value
insert is inserting a new node at a certain position
"""


#given the head of a linked list remove the nth node from the end of the list and return its head

class Solution:
    def removenthnode(self, val, next):
        leftpointer = head
        rightpointer = head
        while n > 0 and rightpointer:
            rightpointer = rightpointer.next
            n -= 1
        
        while rightpointer and rightpointer.next:
            leftpointer = leftpointer.next
            rightpointer = rightpointer.next
        
        if leftpointer == head and not rightpointer:
            return head.next

        lefpointer.next = leftpointer.next.next
        return head


#intersection of two linked lists
#given the heads of two singly linked lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection return null

class Solution2:
    def intersection(self, headA, headB):
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        while pA != pB:
            pA = pA.next if pA.next != None else headB
            pB = pB.next if pB.next != None else headA

        return pA


#find the duplicate number
#given an array of integers nums containing n + 1 integers where each integer is in the range [1,n] inclusive
#there is only one duplicate number in nums, return this duplicate number
#you must solce this problem without modifying the array nums and uses only constant extra space

#its O(n^2) time complexity and O(1) space complexity
class Solution3:
    def findnumber():
        for i in range(0, len(nums)):
            for j in range(1, lwn(nums)):
                if nums[i] == nums[j]:
                    return nums[i]


#its O(n) time complexity and O(n) space complexity
#floyd cycle detection algorithm
def FloydSolution4(nums):
    slowp = 0
    fastp = 0

    while True:
        slowp = nums[slowp]
        fastp = nums[nums[fastp]]
        if slowp == fastp:
            break

    moreslowp = 0
    
    while True:
        slowp = nums[slowp]
        moreslowp = nums[moreslowp]
        if slowp == moreslowp:
            return slowp

nums = [1,3,4,2,2]

print(FloydSolution4(nums))


