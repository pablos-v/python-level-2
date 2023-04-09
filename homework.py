import task_5


class Factory:

    def __init__(self, who, *args):
        self.args = args
        self.who = who

    def create(self):
        if self.who == 'dog':
            return task_5.Dog(*self.args)
        if self.who == 'eagle':
            return task_5.Eagle(*self.args)
        if self.who == 'fish':
            return task_5.Fish(*self.args)


if __name__ == '__main__':
    dog = Factory('dog', 'Bubu', 23)
    bubu = dog.create()
    print(type(bubu))
    bubu.specific()
