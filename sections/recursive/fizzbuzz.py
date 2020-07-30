def fizzbuzz(length):
    if not length:
        return
    else:
        fizzbuzz(length - 1)
        print_val = ""
        if not length % 3:
            print_val += "Fizz"
        if not length % 5:
            print_val += "Buzz"
        print(print_val or length)
