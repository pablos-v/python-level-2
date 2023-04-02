def asker():
    a = int(input('num of tries'))
    b = int(input('num to guess'))

    def game():
        for _ in range(a):
            n = int(input('try to guess:'))
            if n == b:
                print('Wow!')
                return
            print('nope...')
        return

    return game


if __name__ == '__main__':
    play = asker()
    play()
