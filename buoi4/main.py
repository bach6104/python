# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.def so_le(x):
# cho một mảng số nguyên, sau đó ghi những phần tử trong mảng là số nguyên tố vào file nguyento.txt, ghi mới (w)

# Press the green button in the gutter to run the script.
my_array = [1, 2, 3, 4, 5, 6, 7, 8]


def kiem_tra_so_nguyen_to(x):
    if x == 1:
        return False

    for y in range(2, x - 1):
        if x % y == 0:
            return False

    return True


def in_so_nguyen_to(x):
    for y in x:
        if kiem_tra_so_nguyen_to(y):
            f = open("filesonguyento.txt", "w")
            f.write(str(y))
            f.close()
            f = (open("filesonguyento.txt", "r"))
            print(f.read())

    return int(kiem_tra_so_nguyen_to(y))


def kiem_tra_so_hoan_hao(sox):
    tong = 0
    for x in range(1, sox - 1):
        if sox % x == 0:
            tong = tong + x

    if tong == sox:
        return True
    else:
        return False


def tinh_tong(my_array):
    tong = 0
    f = open("insohoanhao", "w")
    for x in my_array:
        if kiem_tra_so_hoan_hao(x):
            tong = tong + x
            f.write(str(x) + '\n' )
    f = open("insohoanhao", "r")
    print(f.read())
    return tong

def viet_invert():
    print("nhập dữ liệu mong muốn:")
    x = input()
    print("bạn vừa nhập", x)
    dao_nguoc = x[::-1]
    f = open("daonguoc.txt", 'w',encoding="utf-8")
    f.write(dao_nguoc)
    f.close()
    openfile = open("daonguoc.txt", 'r', encoding="utf-8")
    print("nội dung của file là ", openfile.read())

    # print("nhập dữ liệu", x)
    # f = open("data.txt","w", encoding="utf-8")
    # f.write(x)
    # f.close()
    # f = open("data.txt", "r", encoding="utf-8")
    # print(f.read())
    # x = input()
    # print("nhập dữ liệu", x)
    # f = open("data.txt","w", encoding="utf-8")
    # f.write(x)
    # f.close()
    # f = open("data.txt", "r", encoding="utf-8")
    # print(f.read())

def

if __name__ == '__main__':
    day_so = [1, 2, 3, 4, 5, 6, 7, 8,24,28]
    # a = in_so_nguyen_to(day_so)
    # a = 'a'
    # b = int(a)
    # print(type(b))
    # a = '10'
    # x = int(a)
    # print(type(x))
    #tong = tinh_tong(day_so)
    #print("tong cua toi la", tong)
    #ketqua = kiem_tra_so_hoan_hao(6)
    #print(ketqua)
    '''
    print('mời nhập thông tin:')
    x = input()
    print("nhập số liệu ", x)
    f = open("data.txt", "w", encodding='utf-8')
    f.write(x)
    f.close()
    f = open("data.txt", "r", encoding="utf-8")
    print(f.read())
    '''
    viet_invert()

