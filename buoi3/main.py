# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.def so_le(x):

# Press the green button in the gutter to run the script.
def calc_array_positive():
    my_array = [-1, -2, 5, 6, 78]
    calc = 0
    sum_array = 0
    for x in my_array:
        if x > 0:
            calc = calc + 1
            sum_array = sum_array + x

    if calc > 0:
        print(sum_array / calc)
    else:
        print("khong co so nao duong")


def is_nguyen_to(x):
    if x <= 1:
        return False
    for y in range(2, x - 1):
        if x % y == 0:
            return False

    return True


def kiem_tra_so_nguyen_to(my_numbers):
    tong = 0
    for x in my_numbers:
        if is_nguyen_to(x):
            tong = tong + x

    print(tong)

def is_hoan_hao(x):
    tong = 0
    for y in range(1, x -1):
        if x % y == 0:
            tong = tong +y

    if tong == x:
        return True
    else:
        return False



def tinh_tong_so_perf(my_array):
    tong = 0

    for x in my_array:
        if is_hoan_hao(x):
            tong = tong + x

    print(tong)



if __name__ == '__main__':
    # calc_array_positive()
    # is_nguyen_to(5)
    so_nguyen_to = [1, 3, 4, 5, 6, 67, 8, 9, 10, 13, 17, 28]
    #kiem_tra_so_nguyen_to(so_nguyen_to)
    #is_hoan_hao(2)
    #print(is_hoan_hao(so_nguyen_to))
    tinh_tong_so_perf(so_nguyen_to)