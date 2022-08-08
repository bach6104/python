# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.def so_le(x):

# Press the green button in the gutter to run the script.\
import math
import os

def kiem_tra_so_nguyen_to(motso):
    if motso == 1:
        return False
    for x in range(2, motso - 1):
        if motso % x == 0:
            return False

    return True


def calc_so_nguyen_to(dayso):
    tong = 0
    calc = 0
    for y in dayso:
        if kiem_tra_so_nguyen_to(y):
            tong = tong + y
            calc = calc + 1

    print(tong / calc)


def kiem_tra_so_hoan_hao(so_hoan_hao):
    tong = 0
    for x in range(1, so_hoan_hao - 1):
        if so_hoan_hao % x == 0:
            tong = tong + x

    if tong == so_hoan_hao:
        return True
    else:
        return False


def calc_so_hoan_hao(my_day_so):
    tong_moi = 0
    calc = 0
    for y in my_day_so:
        if kiem_tra_so_hoan_hao(y):
            tong_moi = tong_moi + y
            calc = calc + 1

    print(tong_moi / calc)


def kiem_tra_so_chan(dso):
    if dso % 2 == 0:
        return True
    else:
        return False


def kiem_tra_so_chia_3(daso):
    if daso % 3 == 0:
        return True
    else:
        return False


def tinh_tb(days):
    tong = 0
    calc = 0
    for q in days:
        if kiem_tra_so_chan(q) and kiem_tra_so_chia_3(q):
            tong = tong + q
            calc = calc + 1

    print(tong / calc)


def kiem_tra_so_le(mso):
    if not kiem_tra_so_chan(mso):
        return True
    else:
        return False


def kiem_tra_so_chia_5(iso):
    if iso % 5 == 0:
        return True
    else:
        return False


def ting_tb_5(array_s):
    tong = 0
    calc = 0
    for x in array_s:
        if kiem_tra_so_chia_5(x):
            tong = tong + x
            calc = calc + 1
    if calc > 0:
        print((tong / calc))
    else:
        print("khong co phan tu chia het cho 5")


def tim_max_phan_tu(my_array):
    max = 0
    for x in my_array:
        if x > max:
            max = x

    print(max)


def tim_min_phan_tu(my_arrays):
    if len(my_arrays) == 0:
        print("khong co doi tuong phu hop")
    else:

        minnums = my_arrays[0]
        for y in my_arrays:
            if y < minnums:
                min = y

        print(minnums)


def kiem_tra_so_max(my_day_so):
    maximum = 0
    for x in my_day_so:
        if x > maximum and x % 2 == 0:
            maximum = x

    print(maximum)


def kiem_tra_so_le_chia_3(my_array):
    if len(my_array) == 0:
        print("khong co gia tri de the hien")
    else:
        if my_array[0] % 3 == 0:
            minimum = my_array[0]
        else:
            minimum = 9999
        for x in my_array:
            if x < minimum and x % 3 == 0:
                minimum = x
        if minimum % 3 == 0:
            print(minimum)
        else:
            print("khong co phan tu phu hop nao")


def myfunc(kiem_so):
    for x in kiem_so:
        if x % 3 == 0 and x % 5 == 0:
            print(x)


def myfuncc(my_array):
    for x in my_array:
        if x % 9 == 0:
            print(x)


def myfuncx(sochan):
    tong = 0
    for x in sochan:
        if x % 2 == 0:
            tong = tong + x

    print(tong)


def kiem_tra_so_le(do):
    if not kiem_tra_so_chan(do):
        return True
    else:
        return False


def calc_so_le(sole):
    tong = 0
    for y in sole:
        if kiem_tra_so_le(y):
            tong = tong + y

    print(tong)


def check_so_nguyen(son):
    x = type(son)
    if x == int:
        return True
    else:
        return False


def tinh_tong_nguyen(lso):
    tong = 0
    for y in lso:
        if check_so_nguyen(y) and y % 3 == 0:
            tong = tong + y

    print(tong)


def calc_so_am(so):
    calc = 0
    for x in so:
        if x > 0:
            calc = calc + 1

    print(calc)

    caalc = 0
    for y in so:
        if y < 0:
            caalc = caalc + 1
        else:
            print("khong co gia tri thoa man")

    print(caalc)


def dem_so_chan_le(so):
    calc_so_chan = 0
    for x in so:
        if kiem_tra_so_chan(x):
            calc_so_chan = calc_so_chan + 1

    print(calc_so_chan)
    tong_so_le = 0
    for y in so:
        if kiem_tra_so_le(y):
            tong_so_le = tong_so_le + 1

    print(tong_so_le)


def goi_so_ngto(slo):
    for idx, x in enumerate(slo):
        if kiem_tra_so_nguyen_to(x):
            print(idx, x)

def testfunc():
    tong = 0
    x = 10
    try:
        print()
        print(x/ tong)
    except (NameError, ZeroDivisionError):
        print("Python Quiz")

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


def tim_so_lon_nhat(dso):
    print("Nhập chữ số của bạn:")
    a = int(input())
    X = max(a)
    for idx, X in enumerate(dso):
        print(X)

if __name__ == '__main__':
    # my_array = [1,2,3,4,5,56,6,7,78,13,23,29]
    # calc_so_nguyen_to(my_array)
    # ket_qua = kiem_tra_so_nguyen_to(29)
    # print(ket_qua)
    day_so = [1, 4, 5, 6, 78, 223, 23, 28, 24, 36, 45, 120, 30, 125]
    # calc_so_hoan_hao(day_so)
    # ket_qua = kiem_tra_so_hoan_hao(6)
    # print(ket_qua)
    # tinh_tb(day_so)
    # ket_qua = kiem_tra_so_le()
    # print(ket_qua)
    # ting_tb_5(day_so)
    # tim_max_phan_tu(day_so)
    # tim_min_phan_tu(day_so)
    # kiem_tra_so_max(day_so)
    # kiem_tra_so_max(day_so)
    # kiem_tra_so_le_chia_3(day_so)
    # myfunc(day_so)
    # myfuncc(day_so)
    # myfuncx(day_so)
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
    tinh_phuong_trinh_bac_2()