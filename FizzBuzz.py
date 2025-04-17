for i in range(101):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
        else:
            print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
