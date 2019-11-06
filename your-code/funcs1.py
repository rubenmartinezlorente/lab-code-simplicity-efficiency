def request_a(str_numbers):
    a = input('Please choose your first number (zero to five): ')
    while a not in str_numbers:
            a = input('''Please, I cannot understand your input, please choose your first number (zero to five): ''')
    return a


def request_b(ops):
    b = input('What do you want to do? plus or minus: ')
    while b not in ops:
            b = input('''Please, I cannot understand your input, please tell me what do you want to do? plus or minus: ''')
    return b



def request_c(str_numbers):
    c = input('Please choose your second number (zero to five): ')
    while c not in str_numbers:
            c = input('''Please, I cannot understand your input, please choose your first number (zero to five): ''')
    return c


def calculation(a,b,c,dict_numbers):
    if b == 'plus':
       return  dict_numbers[a] + dict_numbers[c]
    else:
        return dict_numbers[a] - dict_numbers[c]

def convert_int(dict_numbers,result):
    for el in dict_numbers:
        if dict_numbers[el] == abs(result):
           return  el

def declaration(a,b,c,result_int_to_str,result):
    if result  >= 0:
        return print(f'"{a} {b} {c} equals {result_int_to_str}')
    else :
        return print(f'"{a} {b} {c} equals negative {result_int_to_str}')