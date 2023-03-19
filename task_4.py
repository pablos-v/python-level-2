from task_3 import file_generator


def multi_file_generator(*ex):
    for i in ex:
        file_generator('./RES', i[0], count=i[1])


if __name__ == '__main__':
    multi_file_generator(('txc', 1), ('ggh', 1))
