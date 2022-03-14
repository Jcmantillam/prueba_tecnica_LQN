for number in range(0,101):
    if number % 2 == 0 and number % 5 != 0 :
        print(number, "buzz")
    elif number % 5 == 0:
        print(number, "bazz")
    else:
        print(number)