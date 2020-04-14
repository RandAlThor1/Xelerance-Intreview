def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def fibonacci(max_value):
    total = 2
    first = 1
    second = 1
    if (max_value <= 2):
        return 2
    while (True):
        new = first + second
        if (new > max_value):
            return total
        if(isOdd(new)):
            total += new
        first = second
        second = new


if (__name__ == "__main__"):
    print(fibonacci(22))
