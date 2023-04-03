from random import randint


def count(i: int):
    def decor(func):
        def wrapper(*args, **kwargs):
            ls = []
            for _ in range(i):
                ls.append(func(*args, **kwargs))
            return ls

        return wrapper

    return decor


@count(30)
def gene(a=100):
    return randint(1, a)


if __name__ == '__main__':
    print(gene(23))
