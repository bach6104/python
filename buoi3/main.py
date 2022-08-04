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


if __name__ == '__main__':
    calc_array_positive()