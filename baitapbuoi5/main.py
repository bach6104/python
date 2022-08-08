# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.def so_le(x):

# Press the green button in the gutter to run the script.\
import math
import os

def tinh_phuong_trinh_bac_2():
   try:
       print("nhập số a:")
       a = int(input())
       print("nhập số b:")
       b = int(input())
       print("nhập số c:")
       c = int(input())
       delta = (b*b) - (4*a*c)
       nghiem_1 = (-b - math.sqrt(delta)) / (2 * a)
       nghiem_2 = (-b + math.sqrt(delta)) / (2 * a)
       nghiem_kep = -b / 2*a
       if delta > 0:
           print(nghiem_1, nghiem_2)
   except:
           print("phương trình vô nghiệm")


def max_vitri():
        nhap = int(input("Nhap so x gom ba chu so: "))
        tach = list(str(nhap))
        max = 0
        for idx, i in enumerate(tach):
            if int(i) > max:
                max = int(i)
                t = idx
        print("Chu so lon nhat la: ", max)
        if t == 0:
            print("Va o vi tri hang tram")
        elif t == 1:
            print("Va o vi tri hang chuc")
        elif t == 2:
            print("Va o vi tri hang don vi")


def kiem_tra_md():
    print("Nhập tháng của bạn:")
    a = int(input())
    if a > 12:
        print("Lỗi: không có tháng phù hợp")
    if a == 1:
        print("tháng 1 có 31 ngày")
    if a == 2:
        print("tháng 2 có 28/29 ngày")
    if a == 3:
        print("tháng 3 có 31 ngày")
    if a == 4:
        print("tháng 4 có 30 ngày")
    if a == 5:
        print("tháng 5 có 31 ngày")
    if a == 6:
        print("tháng 6 có 30 ngày")
    if a == 7:
        print("tháng 7 có 31 ngày")
    if a == 8:
        print("tháng 8 có 31 ngày")
    if a == 9:
        print("tháng 9 có 30 ngày")
    if a == 10:
        print("tháng 10 có 31 ngày")
    if a == 11:
        print("tháng 11 có 30 ngày")
    if a == 12:
        print("tháng 12 có 31 ngày")


# def in_so_nguyen_to(motso):
#     if motso == 1:
#         return False
#     print("nhập số nguyên tố mà bạn muốn trình bày:")
#     nhap = int(input())
#     for x in nhap:
#         if kiem_tra_so_nguyen_to():
def viet_so_nguyen():
    x = int(input("mời bạn nhập số:"))
    if type(x)== int:
        print("bạn đã nhập đúng số nguyên")
    if x > 1 and x <100:
        print("bạn đã nhập đúng rồi")
    else:
        int(input("bạn đã nhập sai, vui lòng nhập lại:, (lưu ý số phải từ (1,100))"))

def ktra_am(dso):
    for x in dso:
        if x < 0:
            return True
        else:
            return False
def tinh_tbinh_am(aso):
    tong = 0
    calc = 0
    for y in aso:
        if ktra_am(y):
            tong = tong + y
            calc = calc + 1

    print(tong / calc)

if __name__ == '__main__':

    # calc_so_le(day_so)
    # tinh_tong_nguyen(day_so)
    # calc_so_am(day_so)
    # dem_so_chan_le(day_so)
    # goi_so_ngto(day_so)
    # test(day_so)
    # try:
    #     a = 5
    #     b = 0
    #     a / b
    #     print("đã thử hiện a / b")
    # except:
    #     print("đã xảy ra lỗi")
    #print(os.listdir())
    #testfunc()
    #tinh_phuong_trinh_bac_2()
    #kiem_tra_md()
    #max_vitri()
    #viet_so_nguyen()
    ml = [1,4,5,6,7,8,9,-10,-22,-1,-2,55,-60,-4,-3,-7]
    tinh_tbinh_am(ml)