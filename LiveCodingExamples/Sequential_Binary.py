"""
Sequential Search vs Binary Search:
-----------------------------------
    - Sequential Search: O(n)
    - Binary Search: O(log(n))
    - Binary Search requires a sorted list
    - Binary Search is faster than Sequential Search

Search Codes:
-------------
    - Sequential Search:
        - Search for an element in a list
        - Return True if found, False otherwise
    - Binary Search:
        - Search for an element in a list
        - Return True if found, False otherwise
        - Requires a sorted list
        - Uses the divide and conquer approach
        - Compares the element with the middle element of the list
"""

class SearchingAlgorithms:
    def sequantialSearchUnordered(self, unorderedLİst, number):
        index = 0
        found = False

        while index < len(unorderedLİst) and not found:
            if unorderedLİst[index] == number:
                found = True
            else:
                index += 1
        return found

    def sequantialSearchOrdered(self, orderedList, number):
        index = 0
        found = False
        stop = False

        while index < len(orderedLİst) and not found and not stop:
            if orderedLİst[index] == number:
                found = True
            else:
                if orderedList[index] > number:
                    stop = True
                else:
                    index += 1
        return found

    def binarySearch(self, orderedList, number):
        first = 0
        last = len(orderedList) - 1
        found = False

        while first <= last and not found:
            midPoint = (first + last) // 2
            if orderedList[midPoint] == number:
                found = True
            else:
                if number < orderedList[midPoint]:
                    last = midPoint - 1
                else:
                    first = midPoint + 1
        return found



"""

Hash Table:
-----------
    - Hash Table is a data structure that maps keys to values for highly efficient lookup
    - Hash Table is known as Dictionary in Python
    - O(1) for insert, delete and search
    - Hash Table uses a hash function to compute an index into an array of buckets or slots

"""

class HashTable:
    def __init__(self, size):
        self.size = size
        self.dataMap = [None] * self.size
    
    def hashFunc(self, key):
        myHash = 0
        for letter in key:
            myHash = (myHash + ord(letter) * 23) % len(self.dataMap)
        return myHash

    def setItem(self, key, value):
        index = self.hashFunc(key)
        if self.dataMap[index] == None:
            self.dataMap[index] = []
        self.dataMap[index].append([key, value])

    def getItem(self, key):
        index = self.hashFunc(key)
        if self.dataMap[index] is not None:
            for i in range(len(self.dataMap[index])):
                if self.dataMap[index][i][0] == key:
                    return self.dataMap[index][i][1]
        return None

    def getKeys(self):
        keys = []
        for i in range(len(self.dataMap)):
            if self.dataMap[i]:
                for j in range(len(self.dataMap[i])):
                    keys.append(self.dataMap[i][j][0])
        return keys
    
    def printTable(self):
        for index, value in enumerate(self.dataMap):
            print(index, '->', value)

myHashTable = HashTable(5)

myHashTable.setItem('apple', 10)
myHashTable.setItem('orange', 20)
myHashTable.setItem('car', 30)
myHashTable.setItem('table', 40)

print(myHashTable.getItem('apple'))
print(myHashTable.getItem('orange'))
myHashTable.printTable()
print(myHashTable.getKeys())


#Two Sum Problem:
#----------------
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

class SumSolution:

    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range (1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    def twoSum2(self, nums, target):
        for i in range(0, len(nums)):
            if target - nums[i] in nums:
                return [i, nums.index(target - nums[i])]
        return None

    #for space and time complexity O(n)
    def twoSum3(self, nums, target):
        myHash = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in myHash:
                return [myHash[difference], index]
            myHash[num] = index


twosum = SumSolution()
print(twosum.twoSum([2, 7, 11, 15], 22))
print(twosum.twoSum2([2, 7, 11, 15], 17))
print(twosum.twoSum3([2, 13, 11, 15], 13))


#Encode and Decode TinyURL:
#--------------------------
#TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
#Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work.
#You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

class Codec:

    def __init__(self):
        self.encodingMap = {}
        self.decodingMap = {}
        self.baseUrl = 'http://tinyurl.com/'

    def encode(self, longUrl):
        if longUrl not in self.encodingMap:
            shortUrl = self.baseUrl + str(len(self.encodingMap) + 1)
            self.encodingMap[longUrl] = shortUrl
            self.decodingMap[shortUrl] = longUrl
        return self.encodingMap[longUrl]

    def decode(self, shorturl):
        return self.decodingMap[shorturl]

myUrl = Codec()
print(myUrl.encode('https://recepbattal.com/test/leet/code'))
print(myUrl.decode('http://tinyurl.com/1'))


#Brick Wall:
#-----------
#There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width.
#You want to draw a vertical line from the top to the bottom and cross the least bricks.
#The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.
#If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.
#You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

class BrickWall:
    def leastBricks(self, wall):
        myHashMap = {0:0}
        for row in wall:
            gapCount = 0
            for brick in row[:-1]:
                gapCount += brick
                myHashMap[gapCount] = 1 + myHashMap.get(gapCount,0)
        return len(wall) - max(myHashMap.values())

myWall = BrickWall()
print(myWall.leastBricks([[1, 2, 2, 1],
                          [3, 1, 2],
                          [1, 3, 2],
                          [2, 4],
                          [3, 1, 2],
                          [1, 3, 1, 1]]))
print(myWall.leastBricks([[1],[1],[1]]))