# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.def so_le(x):


if __name__ == '__main__':
    for x in range(0,100):
        # print(x)
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
            continue
        if x % 3 == 0:
            print('Fizz')
            continue
        if x % 5 == 0:
            print("Buzz")
            continue
        else:
            print(x)
