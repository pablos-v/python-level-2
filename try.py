if __name__ == '__main__':
    text = 'Enter number desde 1 hasta 999: '
    TEN = 10
    r = 0
    ONE = 1
    TWO = 2
    THREE = 3
    while not r:
        n = input(text)
        length = len(n)
        n = int(n)
        if n > 0:
            if length == ONE:
                r = n ** TWO
            if length == TWO:
                r = n // TEN * (n % TEN)
            if length == THREE:
                r = int(str(n)[::-1])
    print('Entered', length, '- digit number, result', r)
