"""
Sorting Algorithms:
-------------------
visualgo.net
    - Bubble Sort : O(n^2) 
    - Selection Sort : O(n^2)
    - Insertion Sort : O(n^2)
    - Merge Sort : O(nlog(n))
    - Quick Sort : O(nlog(n))
    - Heap Sort : O(nlog(n))
"""

import random

class SortingAlgo:
    def bubblesort(self, array):
        for i in range(len(array) - 1, 0, -1):
            for j in range(i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array

    def selectionsort(self, array):
        for i in range(len(array) - 1):
            minIndex = i
            for j in range(i+1, len(array)):
                if array[j] < array[minIndex]:
                    minIndex = j
            if minIndex != i:
                array[i], array[minIndex] = array[minIndex], array[i]
        return array

    def insertionsort(self, array):
        for i in range(1, len(array)):
            temp = array[i]
            j = i - 1
            while temp < array[j] and j >= 0:
                array[j + 1] = array[j]
                array[j] = temp
                j -= 1
        return array


    def merge(self, arr1, arr2):
        firstpointer = 0
        secondpointer = 0
        result = []

        while firstpointer < len(arr1) and secondpointer < len(arr2):
            if arr1[firstpointer] < arr2[secondpointer]:
                result.append(arr1[firstpointer])
                firstpointer += 1
            else:
                result.append(arr2[secondpointer])
                secondpointer += 1
        while firstpointer < len(arr1):
            result.append(arr1[firstpointer])
            firstpointer += 1
        while secondpointer < len(arr2):
            result.append(arr2[secondpointer])
            secondpointer += 1
        return result

    def mergesort(self, array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        
        return self.merge(self.mergesort(left), self.mergesort(right))


    def quicksort1(self, array):
        if len(array) <= 1:
            return array
        pivot = array.pop()
        left = []
        right = []
        for item in array:
            if item < pivot:
                left.append(item)
            else:
                right.append(item)
        return self.quicksort(left) + [pivot] + self.quicksort(right)


    def pivot(self, array, start, end):
        swapIndex = start
        for i in range(start+1, end+1):
            if array[i] < array[start]:
                swapIndex += 1
                array[i], array[swapIndex] = array[swapIndex], array[i]
        array[swapIndex], array[start] = array[start], array[swapIndex]
        return swapIndex

    def quicksort2(self,array,left = 0,right = None):
        if right == None:
            right = len(array) - 1
        if left < right:
            swapIndex = self.pivot(array, left, right)
            self.quicksort2(array, left, swapIndex - 1)
            self.quicksort2(array, swapIndex + 1, right)
        return array


    def heapify(self,array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[largest] < array[left]:
            largest = left
        if right < n and array[largest] < array[right]:
            largest = right
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.heapify(array, n, largest)

    def heapsort(self, array):
        n = len(array)

        #Max-heap
        for i in range(n, -1, -1):
            self.heapify(array, n, i)
            #print("Max-heap: ", array)
        #Swap
        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)
            #print("Swap: ", array)
        return array


#K closest points to origin
#given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0,0)
#the distance between two points on the X-Y plane is the Euclidean distance (square root of the sum of squares of the differences between the x and y coordinates)
#you may return the answer in any order. the answer is guaranteed to be unique (except for the order that it is in)
import heapq

class KClosest:
    def kClosest(self, points, k):
        minHeap = []
        for x,y in points:
            distancetoOrigin = (x**2 + y**2)
            minHeap.append(([distancetoOrigin,x,y]))

        heapq.heapify(minHeap)

        result = []
        while k > 0:
            distance, x, y = result.append(heapq.heappop(minHeap)[1:])
            result.append([x,y])
            k -= 1

        return result

#Find Median from Data Stream
#The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values
#Implement the MedianFinder class:
#   - MedianFinder() initializes the MedianFinder object
#   - void addNum(int num) adds the integer num from the data stream to the data structure
#   - double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted
#   - 0 <= num <= 10^5
#   - at most 10^5 calls will be made to addNum and findMedian

class MedianFinder:
    def __init__(self):
        self.smallH = []
        self.largeH = []

    def addNum(self, num:int) -> None:
        heapq.heappush(self.smallH, -num)
        if self.smallHand and self.largeH and -self.smallH[0] > self.largeH[0]:
            value = -1 * heapq.heappop(self.smallH)
            heapq.heappush(self.largeH, value)
            #heapq.heappush(self.smallH, -heapq.heappop(self.largeH))

        if len(self.smallH) > len(self.largeH) + 1:
            value = -1 * heapq.heappop(self.smallH)
            heapq.heappush(self.largeH, value)
            #heapq.heappush(self.largeH, -heapq.heappop(self.smallH))
        if len(self.largeH) > len(self.smallH) + 1:
            value = heapq.heappop(self.largeH)
            heapq.heappush(self.smallH, -value)

    def findMedian(self) -> float:
        if len(self.smallH) > len(self.largeH):
            return -self.smallH[0]
        if len(self.largeH) > len(self.smallH):
            return self.largeH[0]
        return (-self.smallH[0] + self.largeH[0]) / 2