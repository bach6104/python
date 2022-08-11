# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.def so_le(x):

# Press the green button in the gutter to run the script.\
import math
import os
import shlex


def tinh_phuong_trinh_bac_2():
    try:
        print("nhập số a:")
        a = int(input())
        print("nhập số b:")
        b = int(input())
        print("nhập số c:")
        c = int(input())
        delta = (b * b) - (4 * a * c)
        nghiem_1 = (-b - math.sqrt(delta)) / (2 * a)
        nghiem_2 = (-b + math.sqrt(delta)) / (2 * a)
        nghiem_kep = -b / 2 * a
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


def tim_posi():
    nhap = (input("nhập số x gồm 3 chữ số: "))
    tach = list(nhap)
    max = 0
    for idx, x in enumerate(tach):
        if int(x) > max:
            max = int(x)
            y = idx
    print("chữ số lớn nhất là:", max)
    if y == 0:
        print("số này ở vị trí hàng trăm")
    elif y == 1:
        print("số này ở vị trí hàng chục")
    elif y == 2:
        print("số này ở vị trí hàng đơn vị")


def kiem_tra_md():
    print("Nhập tháng của bạn:")
    a = int(input())
    if a > 12 and a < 0:
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


def kiem_tra_so_ngto(dso):
    if dso == 1:
        return False

    for x in range(2, dso - 1):
        if dso % x == 0:
            return False

    return True


def in_so_nguyen_to():
    print("nhập số nguyên tố mà bạn muốn trình bày:")
    nhap = int(input())

    for x in range(1, nhap):
        if kiem_tra_so_ngto(x):
            print(x)


def viet_so_nguyen():
    x = int(input("mời bạn nhập số:"))
    if type(x) == int:
        print("bạn đã nhập đúng số nguyên")
    if x > 1 and x < 100:
        print("bạn đã nhập đúng rồi")
    else:
        int(input("bạn đã nhập sai, vui lòng nhập lại:, (lưu ý số phải từ (1,100))"))


# def ktra_am(dso):
#     for x in dso:
#         if x < 0:
#             return True
#         else:
#             return False
def tinh_tbinh_am(aso):
    tong = 0
    calc = 0
    for y in aso:
        if y < 0:
            tong = tong + y
            calc = calc + 1
    print(tong / calc)


def uoc_chung_max(x, y):
    UCLN = []
    if x >= y:
        for i in range(1, y + 1):
            if x % i == 0 and y % i == 0:
                UCLN.append(x)

        print(UCLN[len(UCLN) - 1])
        return UCLN[len(UCLN) - 1]

    if y >= x:
        for i in range(1, x + 1):
            if y % i == 0 and x % i == 0:
                UCLN.append(y)
        print(UCLN[len(UCLN) - 1])
        return UCLN[len(UCLN) - 1]


def boi_min(x, y):
    return int((x * y) / uoc_chung_max(x, y))


def kiem_tra_so_hoan_hao(x):
    if x == 1:
        return False
    sum = 0
    for y in range(1, x - 1):
        if x % y == 0:
            sum = sum + y

    if sum == x:
        return True
    else:
        return False
    # bước 1: nhập từ bàn phím
    # bước 2: kiểm tra xem đó có phải là số hoàn hảo không
    # bước 3: khởi tạo biến đếm sum = 0
    # bước 4: loop kiểm tra từ (1, x-1)
    # bước 5: kiểm tra x có chia hết cho số y hay không, nếu chia hết thì là sum = sum + x
    # bước 6: sau khi hết vòng for, nếu sum = x, nếu đúng thì return True, không thì return False


def is_perf_num():
    print("vui lòng nhập số a:")
    nhap_so_a = input()
    so_a = int(nhap_so_a)
    if so_a == 1:
        return False
    sum = 0
    for x in range(1, so_a - 1):
        if so_a % x == 0:
            sum = sum + x

    if sum == so_a:
        return True
    else:
        return False

#bước 1: viết hàm kiểm tra số hoàn hảo
#bước 2 : có biến tổng thì check xem biến đó có bằng x hay không
#bước 3: viết hàm gọi ra số hoàn hào
#bước 4: for từ range của 1 đến số mình điền -1
#bước 5: kiểm tra xem y có chia hết cho x không
#bước 6: nếu chia hết thì tong = tong + x
#bước 7: kiểm trả xem tong có bang so mình điền hay không, nếu có thì return True, không thì return False

def check_perf_num(x):
    if x == 1:
        return False
    sum = 0
    for i in range(1, x -1):
        if x % i == 0:
           sum = sum + i

    if sum == x:
        return True
    else:
        return False

#bước 1: nhập vào một số K
#bước 2: for x in số k, kiểm tra xem nó có phải là số hoàn hảo hay không, nếu phải thì print ra x
def goi_so_hoan_hao():
    print("Vui lòng nhập số mong muốn của bạn:")
    x = int(input())
    for k in range(1,x+1):
        if check_perf_num(k):
            print(k)

#bước 1 kiểm tra xem một số có phải là số phong phú hay không
#bước 2 có biến tổng thì kiểm tra xem biến đó tổng có lớn hơn x hay không, nếu lớn hơn thì return True, không thì return False
#bước 3 viết 1 hàm chứa range từ một khoảng nào đấy vf tìm xem có bao nhiêu số phong phú trong không đấy

def check_ab_number(x):
    if x == 1:
        return False
    sum = 0
    for i in range(1, x-1):
        if x % i == 0:
            sum = sum +i

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
#bước 1 check xem số đó có phải là số nguyên hay không
#bước 2 điền vào số có 3 chữ số và split nó ra, nếu không được thì làm hàm list ra và tìm các số của nó
#bước 3 kiểm tra xem tích có bằng tổng không, nếu tổng bằng tích thì return True, không thì False

def check_3rdnumber():
    # a = int(input("nhập số a: "))
    # b = int(input("nhập số b: "))
    # c = int(input("nhập số c: "))
    abc = input("nhập số của bạn")
    tach = list(abc)
    sum = 0
    tich = 1
    for x in tach:
        chuyen_x = int(x)
        sum = sum+ chuyen_x
        tich = tich*chuyen_x
    if sum == tich:
        print(abc, " là số tam hoa")
    else:
        print(abc, " không phải là số tam hoa")
    # tich = a*b*c
    # sum = a+b+c
    # if sum == tich:
    #     print( " là số tam hoa")
    # else:
    #     print(my_arr,' không phải là số tam hoa')

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
    import random
    lower_case =  "abcdefghijklmnopqrstuvwsyz"
    upper_case =  "ABCDEFGHIJKLMNOPQRSTUVWSYZ"
    numebers = "0123456789"
    symbols = '!@#$%^&*?/'
    use_for = lower_case + upper_case + numebers +symbols
    length_for_pass = 8
    password = ''.join(random.sample(use_for, length_for_pass))
    print("mật khẩu được tạo ra của bạn là:", password)
if __name__ == '__main__':
    my_list = [-1, -2, -3, -5, -6, -7, -9, 1, 2, 3, 4, 66, 7, -10]
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
    # print(os.listdir())
    # testfunc()
    # tinh_phuong_trinh_bac_2()
    # kiem_tra_md()
    # max_vitri()
    # viet_so_nguyen()
    ml = [1, 4, 5, 6, 7, 8, 9]
    # tinh_tbinh_am(my_list)
    # tim_posi()
    # in_so_nguyen_to()
    # ketqua = kiem_tra_so_ngto()
    # print(ketqua)
    # kiem_tra_boi_va_uoc()
    # print("hãy nhập số nguyên dương x:")
    # x = int(input())
    # print("hãy nhập số nguyên dương y:")
    # y = int(input())
    # ket_q = uoc_chung_max(x, y)
    # print("ước chung lớn nhất là : ", ket_q)
    # ket_qua = boi_min(x, y)
    # print("bội chung nhỏ nhất là:",ket_qua)
    # print("Vui lòng nhập số bạn chọn:")
    # so = int(input())
    # ket_qua = kiem_tra_so_hoan_hao(so)
    # print(ket_qua)
    # ket_qua = is_perf_num()
    # print(ket_qua)
    # so_a = 0
    # while True:
    #     print("vui lòng nhập a: ")
    #     a = input()
    #     if a.isnumeric():
    #         so_a = str(a)
    #         break
    #     else:
    #         print("thứ bạn nhập không phải là số vui lòng nhập lại")
    #
    # print(type(so_a))
    #goi_so_hoan_hao()
    #goi_so_ab()
    #check_3rdnumber()
    my_sort = [3,2,55,67,113,11,56,33]
    bubble_sort(my_sort)
    #random_pass()