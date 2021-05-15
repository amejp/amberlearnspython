for potato in range(1, 101):
    if potato % 3 == 0 and potato % 5 == 0:
        print("fizzbuzz")
    elif potato % 3 == 0:
        print("fizz")
    elif potato % 5 == 0:
        print("buzz")
    else:
        print(potato)
