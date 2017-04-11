import re

DIC = {chr(x): x-97 for x in range(97, 123)} # создаем словарь со всеми буквами алфавита
DIC2 = {chr(x): x-65 for x in range(65, 91)}
DIC.update(DIC2)

def cEncode(string, key):
    '''шифрование'''
    new_string = ''
    for i in string:
        if i not in DIC:  # если символа нет в словаре оставляем как есть
            new_string += i
            continue
        ch = DIC[i] + key
        if ch > 25:  # букв в алфавите 26 (у нас счет с нуля)
            ch = ch - 26
        new_string += get_key(DIC, ch)
    return new_string


def cDecode(string, key):
    '''расшифровка'''
    new_string = ''
    for i in string:
        if i not in DIC:
            new_string += i
            continue
        ch = DIC[i] - key
        if ch < 0:
            ch = 26 + ch
        new_string += get_key(DIC, ch)
    return new_string


def get_key(dic, val):
    '''получение ключа по значению словаря'''
    for i in dic.items():
        if val in i:
            return i[0]