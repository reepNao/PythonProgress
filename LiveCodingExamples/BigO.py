"""
Big O Notation -> 0()
Time Complexity - Space Complexity
time complexity based on worst case scenario

bigocheatsheet.com
Brute Force -> O(n)
Binary Search -> O(log n)

"""

import math

def bigo(n):
    for i in range(0, n):
        print(i)

#bigo(5)

def bigon2(n):
    for i in range(0, n):
        for j in range(0, n):
            print(i, j)

#bigon2(5)

def bigon3(n):
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                print(i, j, k)

#bigon3(5)


def logn(n):
    a = 0
    while n > 1:
        n = math.floor(n/2)
        a += 1
        print(n)
    print(a)

#logn(8192)


def nlogn(n):
    limit = n
    while n > 1:
        n = math.floor(n/2)
        for i in range(0, limit):
            print(i)

#nlogn(16)

def nfactoriel(n): # O(n)
    if n == 0 or n == 1:
        return 1
    while n > 1:
        n = n * nfactoriel(n-1)
        return n

#print(nfactoriel(5))

#Array, List, Stack, Queue, Deque

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# otherlist = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# mylist.extend(otherlist)
# print(mylist)
import sys

n = 15
mydynamicarray = []
for i in range(0, n):
    mylen = len(mydynamicarray)
    mybyte = sys.getsizeof(mydynamicarray)
    mydynamicarray.append(n)
    print(f"Length: {mylen}, Size in bytes: {mybyte}")