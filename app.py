def fizz_buzz(num):
    # fizz % 3
    # buzz % 5
    # fizzbuss % 3 and % 5
    # todo the logic
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

print(fizz_buzz(15))
