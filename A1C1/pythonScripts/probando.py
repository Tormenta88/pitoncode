def FizzBuzz(x):
    if x % 15 == 0:
        return "FizzBuzz"
    elif x %5 == 0:
        return "Buzz"
    elif x % 3 == 0:
        return "Fizz"

print(FizzBuzz(10))