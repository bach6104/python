# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.def so_le(x):

# Press the green button in the gutter to run the script.\
# câu 1:
# local var là các biến có sẵn và sẽ được dùng ở mọi hàm trong suốt quá trình.
# objec attribute là các đặc điểm có trong một hàm class và có thể được nhập từ bàn phím hoặc gán có sẵn.
# câu 2:
# hàm khởi tạm có tên là __init__()
# câu 3:
# class obj:
# def __init__(self):
# ...
# def do_sth(self):
# main:
# obj.do_sth()
# 8.2
# câu 1:
# class Address:
# def __init__(self, number, streetname):
# self.number = number
# self.streetname = streetname
# câu 2:
# đoán : code sẽ in ra 6:30' bởi vì time là biến được gán sẵn trong hàm print time nên sẽ in ra là 6h30
# kqua : hàm in ra là 5:30...
# câu 3:
# đoán : hàm sẽ in ra là 10h30 vì đây self.time không có gán biến nhưng khi sang hàm print thì có biến time được gán biến dưới main trong cả class clock
# kqua
# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         time = '6h30'
#         print(self.time)
#(b) e chưa biết
#4 code sẽ in ra giờ của boston vì chỉ có giờ boston được in ra còn paris thì không
#kqua: code chạy ra giờ của paris

#
class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self):
        print(self.time)

class Queue:
    def __init__(self, obj):
        self.obj = obj
    def get_obj(self):
        return self.obj


if __name__ == '__main__':
    # clock = Clock('5:30')
    # clock.print_time()
    # clock = Clock('5: 30')
    # clock.print_time('10: 30')
    boston_clock = Clock('5: 30')
    paris_clock = boston_clock
    paris_clock.time = "10: 30"
    boston_clock.print_time()
