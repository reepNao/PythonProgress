"""
in stack last in first out, push&pop methods (top&base) are used = like a stack of plates
in queue first in first out, enqueue&dequeue methods (front&rear) are used = like a line of people
in deque double ended queue, add, remove, addfirst, removefirst, addlast, removelast methods are used = like a line of people but you can add or remove from both ends

Stack():
--------
push(item)
pop()
showLast()
size()
isEmpty()

"""


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def showLast(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

mystack = Stack()


"""
Queue():
--------
enqueue(item)
dequeue()
size()
isEmpty()

"""

class Queue():
    def __init__(self):
        self.items = []
        print(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)
        print(self.items)
    
    def dequeue(self):
        print(self.items.pop())
        
    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

myqueue = Queue()


"""
Deque():
--------
add(item)
remove(item)
addFirst(item)
removeFirst(item)
addLast(item)
removeLast(item)
size()
isEmpty()

"""

class Deque():

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(self.items)

    def remove(self, item):
        self.items.remove(item)
        print(self.items)

    def addFirst(self, item):
        self.items.insert(0, item)
        print(self.items)

    def removeFirst(self, item):
        self.items.pop(0)
        print(self.items)

    def addLast(self, item):
        self.items.append(item)
        print(self.items)

    def removeLast(self, item):
        self.items.pop()
        print(self.items)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

mydeque = Deque()


"""
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft()) #we pop everything but the last one (and also we append them back)
        return self.q.popleft() #we pop the last one and not append it back

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0
"""

#baseball game leetcode


#an integer x -record a new score of x
#string "+" -record a new score that is the sum of the previous two scores
#string "D" -record a new score that is double the previous score
#string "C" -invalidate the previous score, removing it from the record
#return the sum of all the scores on the record
#its a baseball game, so we can use stack to store the scores and their indexes

myinput = ["5", "2", "C", "D", "+"]

def solution(myinput):
    stack = []
    for i in myinput:
        if i == "C":
            stack.pop()
        elif i == "D":
            stack.append(stack[-1]*2)
        elif i == "+":
            stack.append(stack[-1]+stack[-2])
        else:
            stack.append(int(i))
    return sum(stack)

print(solution(myinput))




'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

its daily temperatures, so we can use stack to store the temperatures and their indexes
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # initialize with 0s so we don't have to manually add 0s if none is compliant later on
        myStack = [] #storing pair of temperature and corresponding index 
        
        for ix, temperature in enumerate(temperatures):
            while myStack and temperature > myStack[-1][0]:
                stackTemperature, stackIndex = myStack.pop()
                result[stackIndex] = (ix - stackIndex)
            myStack.append([temperature, ix])
        return result
