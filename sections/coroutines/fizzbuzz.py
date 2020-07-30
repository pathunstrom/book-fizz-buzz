def fizzbuzz_generator():
    value = yield
    while True:
        rv = ""
        if not value % 3:
            rv += "Fizz"
        if not value % 5:
            rv += "Buzz"
        value = yield rv or value


def fizzbuzz():
    cfb = fizzbuzz_generator()
    next(cfb)
    for x in range(101):
        print(cfb.send(x))
