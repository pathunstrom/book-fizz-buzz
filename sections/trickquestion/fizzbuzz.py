def fizzbuzz():
    for i in range(1, 101):
        print_val = ""
        if not i % 3:
            print_val += "Fizz"
        if not i % 5:
            print_val += "Buzz"
        print(print_val or i)
