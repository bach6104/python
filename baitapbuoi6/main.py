# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.def so_le(x):

# Press the green button in the gutter to run the script.\
import math
import os
import shlex


# bước 1 kiểm tra xem một số có phải là số phong phú hay không
# bước 2 có biến tổng thì kiểm tra xem biến đó tổng có lớn hơn x hay không, nếu lớn hơn thì return True, không thì return False
# bước 3 viết 1 hàm chứa range từ một khoảng nào đấy vf tìm xem có bao nhiêu số phong phú trong không đấy

def check_ab_number(x):
    if x == 1:
        return False
    sum = 0
    for i in range(1, x - 1):
        if x % i == 0:
            sum = sum + i

    if sum > x:
        return True
    else:
        return False


def goi_so_ab():
    print("vui lòng nhập số của bạn từ các khoảng")
    a = int(input("khoảng chặn dưới là :"))
    b = int(input("khoảng chặn trên là:"))
    for x in range(a, b):
        if check_ab_number(x):
            print(x)


# bước 1 check xem số đó có phải là số nguyên hay không
# bước 2 điền vào số có 3 chữ số và split nó ra, nếu không được thì làm hàm list ra và tìm các số của nó
# bước 3 kiểm tra xem tích có bằng tổng không, nếu tổng bằng tích thì return True, không thì False

# def check_3rdnumber():
#     # a = int(input("nhập số a: "))
#     # b = int(input("nhập số b: "))
#     # c = int(input("nhập số c: "))
#     abc = input("nhập số của bạn")
#     tach = list(abc)
#     sum = 0
#     tich = 1
#     for x in tach:
#         chuyen_x = int(x)
#         sum = sum+ chuyen_x
#         tich = tich*chuyen_x
#     if sum == tich:
#         print(abc, " là số tam hoa")
#     else:
#         print(abc, " không phải là số tam hoa")
#     # tich = a*b*c
# sum = a+b+c
# if sum == tich:
#     print( " là số tam hoa")
# else:
#     print(my_arr,' không phải là số tam hoa')

def check_so_ngto(motso):
    if motso == 1:
        return False
    for x in range(2, motso - 1):
        if motso % x == 0:
            return False

    return True


def goi_so_ngto():
    print("vui lòng nhập số của bạn từ khoảng:")
    a = int(input("khoảng chặn dưới là:"))
    b = int(input("khoảng chặn trên là:"))
    for i in range(a, b):
        if check_so_ngto(i):
            print(i)


def check_so_am(dso):
    if dso < 0:
        return True

    return False


def goi_so_am(myarr):
    tong = 0
    calc = 0
    for x in myarr:
        if check_so_am(x):
            tong = tong + x
            calc = calc + 1

    print(tong / calc)


def check_so_duong(dayso):
    if dayso > 0:
        return True

    return False


def goi_so_duong(myar):
    tong = 0
    calc = 0
    for x in myar:
        if check_so_duong(x):
            tong = tong + x
            calc = calc + 1

    print(tong / calc)


def goi_so_ngto(my_array):
    tong = 0
    calc = 0
    for x in my_array:
        if check_so_ngto(x) and x > 0:
            tong = tong + x
            calc = calc + 1

    print(tong / calc)


def check_perf_number(motso):
    if motso == 1:
        return False
    sum = 0
    for x in range(1, motso - 1):
        if motso % x == 0:
            sum = sum + x

    if sum == motso:
        return True
    else:
        return False


def goi_so_perf(my_arr):
    tong = 0
    calc = 0
    for x in my_arr:
        if check_perf_number(x):
            tong = tong + x
            calc = calc + 1

    print(tong / calc)


# bước 1 : viếthafafm kiểm tra số chính phương
# bước 2 : for x in my arr, if x*x = myarr, return True, else False hoặc dùng sqrt
# bước 3: viết hàm tính tbinh số chính pưhong

def check_so_chinh_phuong(motso):
    for x in range(1, motso -1):
        if math.sqrt(motso) == x:
            return True
        else:
            return False


def goi_so_chinh_phuong(myarr):
    tong = 0
    calc = 0
    for x in myarr:
        if check_so_chinh_phuong(x):
            tong = tong + x
            calc = calc + 1

    print(tong / calc)


def check_num(moso):
    if moso % 2 == 0 and moso % 3 == 0:
        return True
    else:
        return False


def goi_num(my_arr):
    tong = 0
    calc = 0
    for x in my_arr:
        if check_num(x):
            tong = tong + x
            calc = calc + 1
    print(tong / calc)

#def check_so_fibo():
def check_so_chan(mso):
    if mso %  2 == 0:
        return True
    else:
        return False

def check_so_le(myarr):
    if not check_so_chan(myarr) and myarr % 5 == 0:
        return True
    else:
        return False

def goi_num(myar):
    tong = 0
    calc = 0
    for x in myar:
        if check_so_le(x):
            tong = tong + x
            calc = calc +1

    print(tong/ calc)

def check():
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    s = input('Input a string: ')

    for ch in s:
        if ch in lowercase:
            print(uppercase[lowercase.find(ch)], end='')
        else:
            print(ch, end='')

def check_code():
    import string

    orig_str = input("Palindrome test -- enter a string: ")

    my_str = orig_str.lower()
    for bad_char in string.whitespace + string.punctuation:
        my_str = my_str.replace(bad_char, '')

    # index technique
    front = 0
    end = len(my_str) - 1
    mid = len(my_str) / 2

    while end >= mid:
        if my_str[front] != my_str[end]:
            print(my_str, 'is not a palindrome')
            break
        end -= 1
        front += 1
    else:
        print("It's a palindrome")

def check_so():
    A = 3 * "125"
    print("Value of A:", A)  # Value of A: ____________

    B = 3 * int("125")
    print("Value of B:", B)  # Value of B: ____________

    C = 3 * str(125)
    print("Value of C:", C)  # Value of C: ____________

    D = "a" + "bc" * 2
    print("Value of D:", D)  # Value of D: ____________

    E = ("A" + "BC") * 2
    print("Value of E:", E)  # Value of E: ____________

    F = "a" in "aardvark"
    print("Value of F:", F)  # Value of F: ____________

    G = "ad" in "aardvark"
    print("Value of G:", G)  # Value of G: ____________

    ZZZ = "Arthur, King of the Britons"

    H = ZZZ[:4]
    print("Value of H:", H)  # Value of H: ____________

    I = ZZZ[-3:]
    print("Value of I:", I)  # Value of I: ____________

    J = ZZZ[-6:-2]
    print("Value of J:", J)  # Value of J: ____________

    S1 = "Tiger"
    S2 = "tiger"

    A = S1 == S2
    print("Value of A:", A)  # Value of A: ____________

    B = S1 > S2
    print("Value of B:", B)  # Value of B: ____________

    S3 = "aardvark"
    S4 = "anteater"

    E = S3 == S4
    print("Value of E:", E)  # Value of E: ____________

    S5 = "ants"
    S6 = "anteater"

    H = S5 > S6
    print("Value of H:", H)  # Value of H: ____________

def check_algo():
    # Python program for implementation of Bubble Sort

    def bubbleSort(arr):
        n = len(arr)

        # Traverse through all array elements
        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Driver code to test above
    arr = [34, 64, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

def raddix_check():
    # Python program for implementation of Radix Sort
    # A function to do counting sort of arr[] according to
    # the digit represented by exp.

    def countingSort(arr, exp1):

        n = len(arr)

        # The output array elements that will have sorted arr
        output = [0] * (n)

        # initialize count array as 0
        count = [0] * (10)

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = arr[i] // exp1
            count[index % 10] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            index = arr[i] // exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    # Method to do Radix Sort
    def radixSort(arr):

        # Find the maximum number to know number of digits
        max1 = max(arr)

        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp >= 1:
            countingSort(arr, exp)
            exp *= 10

    # Driver code
    arr = [170, 45, 75, 90, 802, 24, 2, 66]

    # Function Call
    radixSort(arr)

    for i in range(len(arr)):
        print(arr[i], end=" ")

    # This code is contributed by Mohit Kumra
    # Edited by Patrick Gallagher


if __name__ == '__main__':
    # goi_so_ngto()
    my_list = [-1, -2, -3, -4, -5, 12, 13, 14, 56, -10, -11, -12, 20, 7, 5, 3, 2, 6, 28, 15, 30, 35]
    # goi_so_am(my_list)
    # goi_so_duong(my_list)
    # goi_so_ngto(my_list)
    # goi_so_perf(my_list)
    #goi_so_chinh_phuong(my_list)
    #goi_num(my_list)
    #my_array = [1,2,3]
    #goi_num(my_list)
    #check_algo()
    i = 0
    while i < 6:
        print(i)
        i = i +1
