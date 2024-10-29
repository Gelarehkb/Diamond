number = int(input("Diamond size: "))

if number < 2:
    print("Invalid size")
else:
    if number % 2 == 0:
        number += 1

    half = number // 2

    for i in range(half + 1):
        if i == 0:
            print(' ' * half + '*' + ' ' * (half))
        else:
            print(' ' * (half - i) + '*' + ' ' * (2 * i - 1) + '*' + ' ' * (half - i))



    for i in range(half - 1, -1, -1):
        if i == 0:
            print(' ' * half + '*' + ' ' * (half))
        else:
            print(' ' * (half - i) + '*' + ' ' * (2 * i - 1) + '*' + ' ' * (half - i))
