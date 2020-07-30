print("\n".join("FizzBuzz"[i*i % 3*4:8--i**4 % 5] or str(i) for i in range(1, 101)))
