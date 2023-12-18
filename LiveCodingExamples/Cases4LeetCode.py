"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        myHash = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in myHash:
                return [myHash[difference], index]
            myHash[num] = index

class BrickWall(object):
    def leastBricks(self, wall):
        myHashMap = {0:0}
        for row in wall:
            count = 0
            for brick in row[:-1]:
                count += brick
                myHashMap[count] = 1+myHashMap.get(count, 0)
        return len(wall) - max(myHashMap.values())

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

class PolindromeNumber:
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        reversed_num = 0
        original_x = x
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x = x // 10
        return True if original_x == reversed_num else False

