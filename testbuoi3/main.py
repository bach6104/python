# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.def so_le(x):

# Press the green button in the gutter to run the script.
def kiem_tra_so_nguyen_to(motso):
    if motso == 1:
        return False
    for x in range(2, motso - 1):
        if motso % x ==0:
            return False

    return True

def calc_so_nguyen_to(dayso):
    tong = 0
    calc = 0
    for y in dayso:
        if kiem_tra_so_nguyen_to(y):
            tong = tong + y
            calc =calc +1

    print (tong / calc)

def kiem_tra_so_hoan_hao(so_hoan_hao):
    tong = 0
    for x in range(1, so_hoan_hao -1):
        if so_hoan_hao % x ==0:
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
        if dso % 2==0:
            return True
        else:
            return False

def kiem_tra_so_chia_3(daso):
       if daso % 3 ==0:
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
        print(( tong / calc))
    else:
        print("khong co phan tu chia het cho 5")

def tim_max_phan_tu(my_array):
    max = 0
    for x in my_array:
        if x > max:
            max = x

    print(max)

def tim_min_phan_tu(my_arrays):
    if len(my_arrays)== 0:
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
        if x > maximum and x % 2 ==0:
            maximum = x

    print(maximum)

def kiem_tra_so_le_chia_3(my_array):
    if len(my_array) == 0:
        print("khong co gia tri de the hien")
    else:
        if my_array[0] % 3==0:
            minimum = my_array[0]
        else:
            minimum = 9999
        for x in my_array:
            if x < minimum and x % 3 == 0:
                minimum = x
        if minimum % 3 ==0:
            print(minimum)
        else:
            print("khong co phan tu phu hop nao")

def myfunc(kiem_so):
    for x in kiem_so:
        if x % 3 ==0 and x % 5 ==0:
            print(x)

def myfuncc(my_array):
    for x in my_array:
        if x % 9 ==0:
            print(x)

if __name__ == '__main__':
    #my_array = [1,2,3,4,5,56,6,7,78,13,23,29]
    #calc_so_nguyen_to(my_array)
    #ket_qua = kiem_tra_so_nguyen_to(29)
    #print(ket_qua)
    day_so = [1,4,5,6,78,223,23,28,24,36,45,120,30,125]
    #calc_so_hoan_hao(day_so)
    #ket_qua = kiem_tra_so_hoan_hao(6)
    #print(ket_qua)
    #tinh_tb(day_so)
    #ket_qua = kiem_tra_so_le()
    #print(ket_qua)
    #ting_tb_5(day_so)
    #tim_max_phan_tu(day_so)
    #tim_min_phan_tu(day_so)
    #kiem_tra_so_max(day_so)
    #kiem_tra_so_max(day_so)
    #kiem_tra_so_le_chia_3(day_so)
    #myfunc(day_so)
    myfuncc(day_so)