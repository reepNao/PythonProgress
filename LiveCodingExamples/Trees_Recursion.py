"""
Trees and Recursion:
--------------------
    - Trees are a data structure that have a root node, branches, and leaves.
    - The root node is the topmost node in the tree.
    - The branches connect the nodes together.
    - The leaves are the nodes that do not have any children.
    - The height of a tree is the length of the longest path to a leaf.
    - The depth of a node is the length of the path to its root.
    - A recursive function is a function that calls itself.
    - Every recursive function has two parts: the base case and the recursive case.
    - The base case is when the function does not call itself again. This is where the function stops.

Binary Search Tree:
-------------------
    - A binary search tree is a tree where every node has two or fewer children.
    - A binary search tree is a tree that is ordered. The left subtree of a node contains only nodes with values less than the node's value. The right subtree of a node contains only nodes with values greater than the node's value.
    - A binary search tree is a tree that is balanced. The difference between the heights of the left subtree and right subtree is no more than one.
    - A binary search tree is a tree that has no duplicate values.
    - The time complexity of searching a binary search tree is O(log n). This is because at every step, you discard half of the tree.
    - The time complexity of inserting a new node into a binary search tree is O(log n). This is because at every step, you discard half of the tree.
    - The time complexity of deleting a node from a binary search tree is O(log n). This is because at every step, you discard half of the tree.
    - The time complexity of traversing a binary search tree is O(n). This is because you must visit every node in the tree.
    - The space complexity of a binary search tree search, insert, or delete operation is O(1). This is because you only need to store a constant number of nodes in memory.
    - The space complexity of a binary search tree traversal is O(n). This is because you need to store all the nodes in memory.
    - The space complexity of a binary search tree is O(n). This is because you need to store all the nodes in memory.
    - The space complexity of a binary search tree is O(n). This is because you need to store all the nodes in memory.
    - The space complexity of a binary search tree is O(n). This is because you need to store all the nodes in memory.
    - The space complexity of a binary search tree is O(n). This is because you need to store all the nodes in memory.
    - The space complexity of a binary search tree is O(n). This is because you need to store all the nodes in memory.
    - The space complexity of a binary search tree is O(n). This is because you need to store all the nodes in memory.
    - The space complexity of a binary search tree is O(n). This is because you need to store all the nodes in memory.

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return True
        tempNode = self.root
        while True:
            if newNode.value == tempNode.value:
                return False
            if newNode.value < tempNode.value:
                if tempNode.left == None:
                    tempNode.left = newNode
                    return True
                tempNode = tempNode.left
            else:
                if tempNode.right == None:
                    tempNode.right = newNode
                    return True
                tempNode = tempNode.right

    def contains(self,value):
        tempNode = self.root
        while tempNode:
            if value < tempNode.value:
                tempNode = tempNode.left
            elif value > tempNode.value:
                tempNode = tempNode.right
            else:
                return True
        return False

    def minofnode(self, node):
        while self.root.left:
            self.root = self.root.left
        return self.root
    
    def maxofnode(self,node):
        while self.root.right:
            self.root = self.root.right
        return self.root

#    def remove(self, value):

mytree = BinarySearchTree()
print(mytree.insert(10))
print(mytree.insert(10))
print(mytree.insert(15))
print(mytree.insert(2))

print(mytree.contains(10))
print(mytree.contains(19))

print(mytree.root.right.value)
print(mytree.root.value)
print(mytree.minofnode(mytree.root).value)


"""
Recursion:
----------
    - Recursion is when a function calls itself.
    - Every recursive function has two parts: the base case and the recursive case.
    - The base case is when the function does not call itself again. This is where the function stops.
    - The recursive case is when the function calls itself. This is where the function continues.
    - All recursive functions can be rewritten as iterative functions.
    - All iterative functions can be rewritten as recursive functions.
    - The time complexity of a recursive function is O(branches^depth). This is because you must visit every node in the tree.
    - The space complexity of a recursive function is O(depth). This is because you need to store every node in memory.
    - The time complexity of an iterative function is O(branches^depth). This is because you must visit every node in the tree.
    - The space complexity of an iterative function is O(depth). This is because you need to store every node in memory.
    - The time complexity of a recursive function is O(branches^depth). This is because you must visit every node in the tree.
    - The space complexity of a recursive function is O(depth). This is because you need to store every node in memory.
    - The time complexity of an iterative function is O(branches^depth). This is because you must visit every node in the tree.
    - The space complexity of an iterative function is O(depth). This is because you need to store every node in memory.
    - The time complexity of a recursive function is O(branches^depth). This is because you must visit every node in the tree.
    - The space complexity of a recursive function is O(depth). This is because you need to store every node in memory.
    - The time complexity of an iterative function is O(branches^depth). This is because you must visit every node in the tree.
    - The space complexity of an iterative function is O(depth). This is because you need to store every node in memory.
    - The time complexity of a recursive function is O(branches^depth). This is because you must visit every node in the tree.
    - The space complexity of a recursive function is O(depth). This is because you need to store every node in memory.
    - The time complexity of an iterative function is O(branches^depth). This is because you must visit every node in the tree.
    - The space complexity of an
"""

#factorial

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def contigious_sum(arr):
    result_sum = 0
    for i in range(len(arr)):
        result_sum += arr[i]
    return result_sum

    """
    if num == 0:
        return 0
    else:
        return num + contigious_sum(num-1)
    """

print(factorial(5))
print(contigious_sum([0]))


myarray = ["h", "e", "l", "l", "o"]

def reverse_string(myarray, start, end):
    if start > end:
        return
    myarray[start], myarray[end] = myarray[end], myarray[start]
    reverse_string(myarray, start+1, end-1)

def revers2(myarray):
    temp = 0
    i = 0
    j = len(myarray)-1
    while i < j:
        temp = myarray[i]
        myarray[i] = myarray[j]
        myarray[j] = temp
        i, j = i+1, j-1
    return myarray
    
reverse_string(myarray, 0, len(myarray)-1)
print(myarray)
revers2(myarray)
print(myarray)


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)

#Iterative
class Solution:
    def fib(self, n: int) -> int:
        x,y = 0,1

        for i in range(n):
            x,y = y,x+y

        return x

#Memoization - we should include a list of fib number calculations to see the effect
class Solution:
    def fib(self, n: int) -> int:
        def iterativeSolution(n):
            x,y = 0,1
            for i in range(n):
                x,y = y,x+y
            return x
        
        memo = {}

        if n not in memo:
            memo[n] = iterativeSolution(n)

        return memo[n]

class treechange:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #Exit condition
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

######################################################################################################################

class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    
    def __init__(self):
        self.root = None

    def insert(self, value):
        
        newNode = Node(value)
        
        if self.root is None:
            
            self.root = newNode
            return True
        
        tempNode = self.root
        
        while True:
            
            if newNode.value == tempNode.value:
                return False
            
            if newNode.value < tempNode.value:
                if tempNode.left is None:
                    tempNode.left = newNode
                    return True
                tempNode = tempNode.left
            
            else: 
                if tempNode.right is None:
                    tempNode.right = newNode
                    return True
                tempNode = tempNode.right

    def contains(self, value):
        tempNode = self.root
        
        while tempNode:
            if value < tempNode.value:
                tempNode = tempNode.left
            elif value > tempNode.value:
                tempNode = tempNode.right
            else:
                return True
        return False
        
    def minOfNode(self,currentNode):
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode
    
    def maxOfNode(self,currentNode):
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode
    
    def BFS(self):
        currentNode = self.root
        myQueue = []
        values = []
        myQueue.append(currentNode)

        while len(myQueue) > 0:
            currentNode = myQueue.pop(0)
            values.append(currentNode.value)
            if currentNode.left is not None:
                myQueue.append(currentNode.left)
            if currentNode.right is not None:
                myQueue.append(currentNode.right)
        return values
    
    def DFSPreOrder(self):
        values = []
        
        def traverse(currentNode):
            values.append(currentNode.value)
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
        traverse(self.root)
        
        return values
    
    def DFSPostOrder(self):
        values = []
        
        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
            values.append(currentNode.value)
        traverse(self.root)
        return values
    
    def DFSInOrder(self):
        values = []
        
        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            values.append(currentNode.value) 
            if currentNode.right is not None:
                traverse(currentNode.right) 
        traverse(self.root)
        return values

myTree = BinarySearchTree()
myTree.insert(38)
myTree.insert(19)
myTree.insert(69)
myTree.insert(12)
myTree.insert(24)
myTree.insert(59)
myTree.insert(95)
myTree.BFS()
myTree.DFSPreOrder()
myTree.DFSPostOrder()
myTree.DFSInOrder()


'''
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sumOfValues = 0
        
        def traversal(node):
            if not node:
                return
            
            nonlocal sumOfValues
            traversal(node.right)
            temp = node.val
            node.val += sumOfValues
            sumOfValues += temp
            traversal(node.left)
        
        traversal(root)
        return root



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    answer = -float("inf")
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.answer
    
    def dfs(self,node):
        if node is None:
            return 0
        
        left = self.dfs(node.left) 
        right = self.dfs(node.right)
        
        left = max(left,0)
        right = max(right,0)
        
        self.answer = max(self.answer,node.val+left+right)
        
        return node.val + max(left,right)