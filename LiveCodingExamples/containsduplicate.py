#given an integer array nums, return True if an yvalue appears at least twice in the array and return false. if every element is distinct

def containsDuplicate(nums):
    for i in range (0, len(nums)):
        for j in range (1, len(nums)):
            if nums [i] == nums[j]:
                return True
            else:
                return False

def containsDuplicate2(nums):
    nums.sort()
    i = 1
    x = nums[0]
    y = nums[i]
    while x < len(nums):
        if x == y:
            return True
        x += 1
        y += 1
    return False

def containsDuplicate3(nums):
    hashSet = set()
    for i in range (0, len(nums)):
        if nums[i] in hashSet:
            return True
        hashSet.add(nums[i])
    return False

def sololine(nums):
    return len(nums) != len(set(nums))

# print(containsDuplicate([1,2,3,4,5]))
# print(containsDuplicate2([1,2,1,4]))
# print(containsDuplicate3([1,2,3,4,5,6,7,8,9,1]))
# print(sololine([1,2,3,4,5,6,7,8,9,1]))



#given a non-empty array of integers nums, every element appears twice except for one. find that single one.
#you must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumbers(nums):
    hashSet = set()
    if len(nums) == 1:
        return nums[0]
    for i in range(0, len(nums)):
        if nums[i] in hashSet:
            hashSet.remove(nums[i])
        else:
            hashSet.add(nums[i])
    return hashSet.pop()

def singleNumbers2(nums):
    result = 0
    for num in nums:
        result ^= num
    return result 
#bit manipulation

print(singleNumbers2([1,1,2,3,3,2,5]))
print(singleNumbers([1,1,2,3,3,5,2]))


#given an array nums of size n, return the majority element.
#the majority element is the element that appears more than n/2 times. you may assume that the majority element always exists in the array.

def majorityElement(nums):
    numbers = {}
    result = 0
    maxnumber = 0

    for i in nums:
        numbers[i] = 1 + numbers.get(i, 0)
        if numbers[i] > maxnumber:
            maxnumber = numbers[i]
            result = i
        maxnumber = max(maxnumber, numbers[i])
    return result

print(majorityElement([1,2,3,4,5,6,7,8,9,1,1,1,1,1,1,1,1,1,1,1]))


def boyermoore(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

print(boyermoore([1,2,3,4,5,6,7,6,6,6,6,6,6,6,1,1,1,1]))
