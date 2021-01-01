def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)

if __name__ == '__main__':
    x = factorial(5)
    print(x)