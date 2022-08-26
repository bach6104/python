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
# (b) e chưa biết
# 4 code sẽ in ra giờ của boston vì chỉ có giờ boston được in ra còn paris thì không
# kqua: code chạy ra giờ của paris

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


class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + '' + self.incantation + '\n' + self.get_description()

    def get_description(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'


def study_spell(Spell):
    print(Spell)

# Radix sort in Python


# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

#  HERE
# + SHE
# -----
# COMES

C = 1
while C <= 9:
    E = 0
    while E <= 9:
        H = 0
        while H <= 9:
            M = 0
            while M <= 9:
                O = 0
                while O <= 9:
                    R = 0
                    while R <= 9:
                        S = 0
                        while S <= 9:
                            #print("CEHMORS:",C,E,H,M,O,R,S)
                            if ((H*1000 + E*100 + R*10 + E) + (S*100 + H*10 + E) == C*10000 + O*1000 + M*100 + E*10 + S)\
                               and C != E and C != H and C != M and C != O and C != R and C != S \
                               and E != H and E != M and E != O and E != R and E != S \
                               and H != M and H != O and H != R and H != S \
                               and M != O and M != R and M != S \
                               and O != R and O != S \
                               and R != S:
                                print("SOLUTION CEHMORS:",C,E,H,M,O,R,S)
                                C,E,H,M,O,R,S = 10,10,10,10,10,10,10
                            else:
                                S += 1
                        R += 1
                    O += 1
                M += 1
            H += 1
        E += 1
    C += 1

#saas , paas, iass
if __name__ == '__main__':
    # clock = Clock('5:30')
    # clock.print_time()
    # clock = Clock('5: 30')
    # clock.print_time('10: 30')
    # boston_clock = Clock('5: 30')
    # paris_clock = boston_clock
    # paris_clock.time = "10: 30"
    # boston_clock.print_time()
    spell = Accio()
    spell.execute()
    study_spell(spell)
    study_spell(Confundo())
    print(Accio)
#get des của confundo được gọi ra khi nhập hàm study spell thì sẽ print nội dung get của confundo ra
    data = [121, 432, 564, 23, 1, 45, 788]
    radixSort(data)
    print(data)