# Урок 2. Файловое хранение данных

# 01.CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
# и формирующий новый «отчетный» файл в формате CSV. Для этого:
# - Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
# В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список.
# Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
# В этой же функции создать главный список для хранения данных отчета — например,
# main_data — и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
# - Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# - Проверить работу программы через вызов функции write_to_csv().
import os
import re
import csv

def get_data(path):
    fnames = os.listdir(path)
    print(fnames)
    headers_list = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for fname in fnames:
        if fname[-3:] == 'txt':
            with open(path+fname, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith('Изготовитель системы'):
                        result = line.split(':')[-1].strip()
                        os_prod_list.append(result)
                    elif line.startswith('Название ОС'):
                        result = line.split(':')[-1].strip()
                        os_name_list.append(result)
                    elif line.startswith('Код продукта'):
                        result = line.split(':')[-1].strip()
                        os_code_list.append(result)
                    elif line.startswith('Тип системы'):
                        result = line.split(':')[-1].strip()
                        os_type_list.append(result)

                    #     result = re.split(r'Изготовитель системы:[ ]*', line)[-1].strip()

    main_data = [headers_list, os_prod_list, os_name_list, os_code_list, os_type_list]
    print(main_data)
    return main_data

def write_to_csv(data_dir_path, csv_file_path):
    with open(csv_file_path, 'w') as fcsv:
        writer = csv.writer(fcsv)
        writer.writerows(get_data(data_dir_path))


data_dir_path = 'files/'
csv_file_path = 'files/csv_data.csv'
write_to_csv(data_dir_path, csv_file_path)


# 02.JSON. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
# Для этого:
# - Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
# - Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json
import pprint


def write_order_to_json(item, quantity, price, buyer, date):
    data = [{'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}]
    with open('files/orders.json', 'r') as fjson:
        fdata= json.load(fjson)
        print(fdata)
        fdata['orders'] += data

    with open('files/orders.json', 'w') as fjson:
        json.dump(fdata, fjson, indent=4)

write_order_to_json('car', 3, 1500000, 'Ivan', '12-06-19')


# 03.YAML. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
# - Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
# третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
# - Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
# - Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
import yaml

data = {'data': [[], 12, {12: '€'}]}
fpath = 'files/yaml_data.yml'
with open(fpath, 'w', encoding='utf-8') as fyaml:
    yaml.dump(data, fyaml, allow_unicode = True, default_flow_style=True)

with open(fpath, 'r', encoding='utf-8') as fyaml:
    read_data = yaml.load(fyaml, Loader=yaml.Loader)
    print(read_data)
    print(read_data == data)