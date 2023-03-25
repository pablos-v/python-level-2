"""Напишите функцию, которая ищет json файлы в указанной директории
 и сохраняет их содержимое в виде одноимённых pickle файлов."""
import json
import os
import pickle


def json_to_pickle(dir_from, dir_to):
    if not os.path.exists(dir_to):
        os.mkdir(dir_to)
    for file in os.listdir(dir_from):
        if file.endswith(".json"):
            with open(file, 'r', encoding='utf-8') as js_f:
                file_content = json.load(js_f)
                print(file_content)  # check
            with open(f'{dir_to}{file.strip(".json")}.pickle', 'wb') as picle_f:
                pickle.dump(file_content, picle_f)
    if os.path.exists(dir_to):  # check
        for file in os.listdir(dir_to):  # check
            with open(f'{dir_to}{file}', 'rb') as f:  # check
                print(pickle.load(f))  # check


if __name__ == '__main__':
    json_to_pickle('./', './task_5/')
