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
        for j in range(0, i - x - 1):
            if my_array[j] > my_array[j + 1]:
                my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]

    print("Dãy số đã được xếp là: ")
    for x in range(len(my_array)):
        print("%d" % my_array[x], end=' ')


def random_pass():
    lower_case = "abcdefghijklmnopqrstuvwsyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWSYZ"
    numebers = "0123456789"
    symbols = '!@#$%^&*?/'
    use_for = lower_case + upper_case + numebers + symbols
    length_for_pass = 8
    password = ''.join(random.sample(use_for, length_for_pass))
    print("mật khẩu được tạo ra của bạn là:", password)


def test(my_arr):
    my_list = ['str', 'chuỗi', 'mảng', 'xâu']
    i = 0
    while True:
        print(my_list[i])
        i = i + 1
        if i >= len(my_list):
            break


def check(my_arr):
    x = my_arr.sort(reverse=True)
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
        while x < len(nums) - 1:
            sum = nums[x] + nums[x + 1]
            if sum == target:
                result.append(x)
                result.append(x + 1)
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
            if idx >= len(self.nums) - 1:
                break
            sum = self.nums[idx] + self.nums[idx + 1]
            if sum == self.target:
                result.insert(0, idx)
                result.insert(1, idx + 1)
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
            nums[idx] = x * x

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


class Pupil:
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def get_attri(self):
        print("Họ của sinh viên là: ", self.last_name)
        print("Tên của sinh viên là: ", self.first_name)
        print("tuổi của sinh viên là: ", self.age)

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def get_own_attr(self):
        return self.first_name, self.last_name, self.age

    def set_last(self, last_name):
        self.last_name = last_name


class SoHoc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __init__(self):
        self.num1 = 10
        self.num2 = 20

    def get_atr(self):
        print("Số đầu tiên là:", self.num1)
        print("số thứ 2 là :", self.num2)

    def set_atr(self, numb1, numb2):
        self.num1 = numb1
        self.num2 = numb2

    def InputInfo(self):
        self.num1 = int(input("nhập số thứ nhất:"))
        self.num2 = int(input("nhập số thứ 2:"))
        print(self.num1, self.num2)

    def addition(self):
        sum = self.num1 + self.num2
        return sum

    def subtract(self):
        sub = self.num1 - self.num2
        return sub

    def mul(self):
        mul = self.num1 * self.num2
        return mul

    def div(self):
        div = self.num1 / self.num2
        return div


class Vector:
    def __init__(self, pra_x, pra_y):
        self.x = pra_x
        self.y = pra_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return "({:.2f}, {:.2f})".format(self.x, self.y)

    def __repr__(self):
        return "({},{})".format(self.x, self.y)

    def __add__(self, v):
        vector_final = Vector(self.x + v.get_x(), self.y + v.get_y())
        return vector_final

    def __sub__(self, v):
        vector_fin = Vector(self.x - v.get_x(), self.y - v.get_y())
        return vector_fin

    def __mul__(self, v):
        qs = Vector(self.x * v.get_x(), self.y * v.get_y())
        return qs

    def __mul_f__(self, number_float: float):
        self.number_float = 10.22

    def __Rmul__(self, number_float: float):
        lo = Vector(self.x * number_float, self.y * number_float)
        return lo

    def __rmul__(self, v):
        ks = self.__mul__(v)
        return ks

    def __eq__(self, v):
        rf = self.x == v.get_x() and self.y == v.get_y()
        return rf


class Student:
    def __init__(self):
        pass

    def input_info(self):
        while True:
            student_id = input("id của học sinh: ")
            if len(student_id) == 8:
                print("mã định danh của học sinh là", student_id)
            else:
                raise Exception("mã định danh không phù hợp")
            student_score = float(input("điểm trung bình của học sinh:"))
            if 0 < student_score < 10:
                print("điểm trung bình cuả học sinh là:", student_score)
            else:
                raise Exception("điểm không hợp lệ")
            student_age = int(input("tuổi của sinh viên là:"))
            if student_age > 18:
                print(student_age)
            else:
                raise Exception("sinh viên không có trên hệ thống")

            student_class = input("lớp của  học sinh là:")
            if student_class[0] == "A" or student_class[0] == "C":
                print("lớp của học sinh là", student_class)
            else:
                raise Exception("lớp không tồn tại")
            break


def f1():
    x = 42

    # nested function
    def f2():
        nonlocal x
        x = 0
        print(x)  # x is now 0
    f2()
    print(x)

if __name__ == '__main__':
    my_list = [-1, -2, -3, -5, -6, -7, -9, 1, 2, 3, 4, 66, 7, -10]
    ml = [1, 4, 5, 6, 7, 8, 9]
    my_sort = [3, 2, 55, 67, 113, 11, 56, 33]
    # bubble_sort(my_sort)
    # random_pass()
    # test(my_list)
    # check(my_sort)
    arr = [10, 0, 9, -15, 10, 10]
    nums = [-4, 0, 3, 10]

    # check_int(arr)
    # p1 = Student('Nguyen', 'Bach',18)
    # x = p1.get_attri()
    # px = Student("Nguyen", "Bach", 18)
    # x = px.get_first_name()
    # print("tên của học sinh:", x)
    # y = px.get_last_name()
    # z = px.get_age()
    # print("họ của học sinh là :", y)
    # print("tuổi của học sinh:", z)
    # first_name, last_name, age = px.get_own_attr()
    # print("Tên của học sinh là: {fn}-"
    #       "Họ của học sinh là: {ln}-"
    #       "Tuổi của học sinh là:{age}".format(fn=first_name,
    #                                           ln=last_name, age=age))
    #
    # px.set_last("Dang")
    # print(px.get_last_name())
    # print("Tên của học sinh là: {fn}-"
    #       "Họ của học sinh là: {ln}-"
    #       "Tuổi của học sinh là:{age}".format(fn=px.get_first_name(),
    #                                           ln=px.get_last_name(), age=px.get_age()))

    # p6 = SoHoc()
    # # o = p6.InputInfo()
    # # print(p6.set_atr(20,10))
    # print("tổng của phép tính là:", p6.addition())
    # print("Hiệu của phép tính là: ",p6.subtract())
    # print("tích của phép tính là:",p6.mul())
    # print("thương của phép tính là:", p6.div())
    # vector_1 = Vector(1, 2)
    # vector_2 = Vector(2.12, 3.12009)
    # p1 = Vector.return_str(vector_1, vector_2)
    # print(p1)
    # p1 = vector_2.__str__()
    # print(p1)
    # p2 = vector_2.__repr__()
    # print(p2)
    # p3 = vector_2.__add__(vector_1)
    # print("Vector 1 là ", vector_1.__str__())
    # print("Vector 2 là ", vector_2.__str__())
    # print(" tổng của 2 vector là", p3.__str__())
    # p4 = vector_2.__sub__(vector_1)
    # print(" hiệu của 2 vector là", p4.__str__())
    # p5 = vector_2.__mul__(vector_1)
    # print("tích của 2 vector là:", p5)
    # p6 = vector_2.__rmul__(vector_1)
    # print("tích của vector là:", p6)
    # p7 = vector_2.__Rmul__(10.22)
    # print(p7)

    # sv = Student()
    # try:
    #     sv.input_info()
    # except Exception as e:
    #     print("co van de, yeu cau nhap lai")
# bước 1: cho nhập số
# bước 2: nếu nhập sai thì bắt nhập lại
# bước 3: nếu nhập sai quá 5 lần thì
    f1()
#các thuật toán sử dụng nhiều: Bubble sort, selection sort, insertion sort,binary tree sort, heap sort, quick sort