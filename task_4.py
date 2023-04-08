import task_3


class Employer(task_3.Person):
    def __init__(self, age, name, address, id_num):
        # task_3.Person.__init__(self, age, name, address)
        super().__init__(age, name, address)
        self.id_num = id_num
        self.access_level = sum((int(i) for i in str(id_num))) % 7

    def all_data(self):
        return f'{self.get_age()}, {self.full_name()}, {self.get_address()}, {self.id_num}, {self.access_level}'


if __name__ == '__main__':
    emp = Employer(21, 'Petr', 'Lenina 5', 143654)
    print(emp.all_data())
