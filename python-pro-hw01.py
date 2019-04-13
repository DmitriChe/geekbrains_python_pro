# 1.    Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
#       соответствующих переменных.
#       Затем с помощью онлайн-конвертера преобразовать строковые представление
#       в формат Unicode и также проверить тип и содержимое переменных.
s1, s2, s3 = 'разработка', 'сокет', 'декоратор'
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))

s1_unicode = '%u0440%u0430%u0437%u0440%u0430%u0431%u043E%u0442%u043A%u0430'
s2_unicode = '%u0441%u043E%u043A%u0435%u0442'
s3_unicode = '%u0434%u0435%u043A%u043E%u0440%u0430%u0442%u043E%u0440'
print(s1_unicode, type(s1_unicode))
print(s2_unicode, type(s2_unicode))
print(s3_unicode, type(s3_unicode))


# 2.    Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования
#       в последовательность кодов (не используя методы encode и decode)
#       и определить тип, содержимое и длину соответствующих переменных.
s1_byte = b'class'
s2_byte = b'function'
s3_byte = b'method'
print(type(s1_byte), s1_byte, len(s1_byte))
print(type(s2_byte), s2_byte, len(s2_byte))
print(type(s3_byte), s3_byte, len(s3_byte))


# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
s1_byte = b'attribute'
# s2_byte = b'класс'  # выдается ошибка, что в байтовый тип можно записать только символы таблицы ASCII
# s3_byte = b'функция'  # выдается ошибка, что в байтовый тип можно записать только символы таблицы ASCII
s4_byte = b'type'
print(type(s1_byte), s1_byte, len(s1_byte))
print(type(s2_byte), s2_byte, len(s2_byte))
print(type(s3_byte), s3_byte, len(s3_byte))
print(type(s4_byte), s4_byte, len(s4_byte))


# 4.    Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
#       в байтовое и выполнить обратное преобразование (используя методы encode и decode).
s1_str = 'разработка'
s2_str = 'администрирование'
s3_str = 'protocol'
s4_str = 'standard'
s1_enc = s1_str.encode()
s2_enc = s2_str.encode()
s3_enc = s3_str.encode()
s4_enc = s4_str.encode()
print(type(s1_enc), s1_enc)
print(type(s2_enc), s2_enc)
print(type(s3_enc), s3_enc)
print(type(s4_enc), s4_enc)
s1_dec = s1_enc.decode()
s2_dec = s2_enc.decode()
s3_dec = s3_enc.decode()
s4_dec = s4_enc.decode()
print(type(s1_dec), s1_dec)
print(type(s2_dec), s2_dec)
print(type(s3_dec), s3_dec)
print(type(s4_dec), s4_dec)

# 5.    Выполнить пинг веб-ресурсов yandex.ru, youtube.com
#       и преобразовать результаты из байтовового в строковый тип на кириллице.
import subprocess


args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

args = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

# 6.    Создать текстовый файл test_file.txt, заполнить его тремя строками:
#       «сетевое программирование», «сокет», «декоратор».
#       Проверить кодировку файла по умолчанию.
#       Принудительно открыть файл в формате Unicode и вывести его содержимое.
import locale


f = open("test_file.txt", "w+")
f.write("сетевое программирование\n")
f.write("сокет\n")
f.write("декоратор\n")

f_coding = locale.getpreferredencoding()
print(f'Кодировка созданного файла по умолчанию: {f_coding}')

f.close()

# При попыткре принудительно открыть файл в кодировке Unicode (utf-8) получаем ошибку, поэтому указываю кодировку файла.
with open('test_file.txt', encoding=f_coding) as f:
    print('\nСодержимое файла:')
    for str_ in f:
        print(str_, end='')
