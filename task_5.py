import task_2
import task_3
import task_4


@task_2.deco
@task_4.count(5)
@task_3.deco
def game(a: int, b: int):
    for _ in range(a):
        n = int(input('try to guess:'))
        if n == b:
            print('Wow!')
            return
        print('nope...')
    return


if __name__ == '__main__':
    a = 3
    b = 30
    game(a, b)
