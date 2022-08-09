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
# bước 2 : for x in my arr, if x*x = myarr, return True, else False
# bước 3: viết hàm tính tbinh số chính pưhong

def check_so_chinh_phuong(motso):
    for x in motso:
        if int(x) * int(x) == int(motso):
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


if __name__ == '__main__':
    # goi_so_ngto()
    my_list = [-1, -2, -3, -4, -5, 12, 13, 14, 56, -10, -11, -12, 20, 7, 5, 3, 2, 6, 28]
    # goi_so_am(my_list)
    # goi_so_duong(my_list)
    # goi_so_ngto(my_list)
    # goi_so_perf(my_list)
    # goi_so_chinh_phuong(my_list)
    goi_num(my_list)
