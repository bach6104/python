# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.def so_le(x):

# Press the green button in the gutter to run the script.\
import math
import os
import shlex
import random

def bubble_sort(my_array):
    i = len(my_array)
    for x in range(i):
        for j in range(0,i - x - 1):
            if my_array[j] > my_array[j + 1]:
                my_array[j] , my_array[j +1] = my_array[j +1], my_array[j]

    print("Dãy số đã được xếp là: ")
    for x in range(len(my_array)):
        print("%d" % my_array[x], end= ' ')

def random_pass():
    lower_case =  "abcdefghijklmnopqrstuvwsyz"
    upper_case =  "ABCDEFGHIJKLMNOPQRSTUVWSYZ"
    numebers = "0123456789"
    symbols = '!@#$%^&*?/'
    use_for = lower_case + upper_case + numebers +symbols
    length_for_pass = 8
    password = ''.join(random.sample(use_for, length_for_pass))
    print("mật khẩu được tạo ra của bạn là:", password)

def test(my_arr):
    my_list = ['str', 'chuỗi', 'mảng', 'xâu']
    i = 0
    while True:
        print(my_list[i])
        i = i +1
        if i >= len(my_list):
            break

def check(my_arr):
    x = my_arr.sort(reverse= True)
    print(x)
    def myfunc(n):
        return abs(n - 50)

    thislist = [100, 50, 65, 82, 23]

    thislist.sort(key=myfunc)

    print(thislist)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        x = 0
        result = []
        while x < len(nums)-1:
            sum = nums[x] + nums[x +1]
            if sum == target:
                result.append(x)
                result.append(x +1)
            x = x + 1
        return result

class SumNumbers:
    def __init__(self, numbs, target):
        self.nums = numbs
        self.numbs = 1
        self.target = target
    def get_nums(self):
        return self.numbs
    def tong_2_sum(self) -> list[int]:
        result = []
        for idx, x in enumerate(self.nums):
            if idx >= len(self.nums)-1:
                break
            sum = self.nums[idx] + self.nums[idx +1]
            if sum == self.target:
                result.insert(0, idx)
                result.insert(1, idx +1)
        return result


class Duplicate:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for x in nums:
            y = nums.count(x)
            if y > 1:
                return True

        return False


class Count:
    def majorityElement(self, nums: list[int]) -> int:
        for x in nums:
            Max = 0
            y = nums.count(x)
            if y > Max:
                Max = x
        return Max


class Sort:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        for idx, x in enumerate(nums):
           nums[idx] = x*x

        nums.sort()
        return nums

def append_list(mso):
    my_list = []
    for x in mso:
        my_list.append(x)
    print(my_list)
    print(type(my_list))

def check_int(dayso):
    for x in dayso:
        if dayso.count(x) > 2:
            return True
        else:
            return False


if __name__ == '__main__':
    my_list = [-1, -2, -3, -5, -6, -7, -9, 1, 2, 3, 4, 66, 7, -10]
    ml = [1, 4, 5, 6, 7, 8, 9]
    my_sort = [3,2,55,67,113,11,56,33]
    #bubble_sort(my_sort)
    #random_pass()
    #test(my_list)
    #check(my_sort)
    arr = [10,0,9,-15,10,10]
    nums = [-4, 0, 3, 10]
    #p1 = Solution()
    #print(p1.twoSum(arr, 26))
    p2 = SumNumbers(nums,-5)
    #print(p2.tong_2_sum())
    #print(p2.get_nums())
    p3 = Duplicate()
   #print(p3.containsDuplicate(arr))
    p4 = Count()
    #print(p4.majorityElement(arr))
    p5 = Sort()
    #print(p5.sortedSquares(nums))
    #print(nums[0:3])
    #nums.append(11)
    #print(nums)
    #nums.reverse()
    #print(nums)
    #byte_array = bytearray(ml)
    #print(len(byte_array))
    #print(id(arr))
    #x = arr.count(10)
    #print(x)
    #nums.extend(nums)
    #print(nums)
    #nums.insert(1, arr)
    #print(nums)
    #nums.remove(10)
    #print(nums)
    #del nums[2]
    #print(nums)
    #arr.pop(10)
    #print(arr)
    #append_list(my_list)
    check_int(arr)