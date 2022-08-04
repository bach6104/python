# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.def so_le(x):
def so_le(x):
    if x % 2 == 0:
        return False
    else:
        return True


def tinh_tong_le(my_array):
    tong = 0
    for x in my_array:
        if so_le(x):
            tong = tong + x

    print(tong)


def so_chan(z):
    if z % 2 == 0:
        return True
    else:
        return False


def tinh_tong_chan(my_array):
    tong = 0
    count = 0
    for z in my_array:

        if so_chan(z):
            tong = tong + z
            count = count + 1

    print(tong / count)


# for 0 -> x-1
# lan luot kiem tra cac vong dieu kien xem x co chia het cho y khong, neu chia het thi cong lay tong hien tai + voi y
# sau khi het vong lap for thi kiem tra tong voi x xem co bang nhau hay khong, neu bang nhau thi la so hoan hao, neu khong thi nguoc lai
def so_hoan_hao(x):
    tong = 0
    for y in range(1, x - 1):
        if x % y == 0:
            tong = tong + y

    if tong == x:
        return True
    else:
        return False


def tinhtongcacsohoanhao(myarray):
    tong = 0
    for x in myarray:
        if so_hoan_hao(x):
            tong = tong + x

    print(tong)


thisdist = {
    "brand": "Ford",
    "type": "Sword",
    "year": 1800,
}

x = thisdist.values()
print(x)

# thisdist["brand"] = "Nike"
thisdist.update({"brand": "Nile"})
print(x)

mylist = {"0": "Minh", "1": "Ha", "2": "Vu", "3": "Thang", "4": "Tuan", "5": "Duc", "6": "Tuan Phuong"}


def datacheck(my_list):
    print(my_list.values())
    print(my_list.keys())
    print(my_list.items())
    for x in my_list.keys():
        data = my_list.get(x)
        if data == "Tuan":
            my_list.update({x: "Tuan1"})
    for x in my_list.get(x):
        # mylist[x] = "Tuan1"
        print(my_list)


def doi_ten(txt):
    x = txt[::-1]
    print(x)


def so_sanh_tu():
    z = "Nguyen Dang Gia Bach"
    my_array = z.split(" ")
    print(my_array)
    vi_tri = 0
    for y in range(0, len(my_array)):
        print(my_array[y])
        if len(my_array[y]) > len(my_array[vi_tri]):
            vi_tri = y
    print(vi_tri)

def viet_hoa(viethoachucaidau):
    myname = "ha anh tuan"
    biendoi = myname.split()
    print(biendoi)
    result = ""
    for x in biendoi:
        result = result + " " + x.capitalize()

    print(result.strip())

def dem_so():
    myrn = "Nguyen Dang Gia Bach"
    print(len(myrn))
    tong_so = 0
    for x in myrn:
        if x == x:
            tong_so = tong_so + 1
        else:
            return False

    print((tong_so))




str_ = "MillieB11"
arr = list(str_)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_array = [2, 3, 4, 5, 6, 7, 8, 9, 212]
    # tinh_tong_le(my_array)
    # tinhtongcacsohoanhao(my_array)
    # inh_tong_chan(my_array)
    # print(thisdist)
    # datacheck(mylist)
    # mystring = "Gia Bach"
    # doi_ten(mystring)
    #sprigga = "Nguyen Dang Gia Bach"
    #so_sanh_tu()
    #print(arr)
    #myname = "ha anh tuan"
    #viet_hoa(myname)
    ten_cua_toi = "Nguyen Dang Gia bach"
    dem_so()
