#Program kalkulator

import logging
logging.basicConfig(level=logging.DEBUG)

op_num = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))

def math_operation(op_num):
    if op_num == 1:
        logging.info("Wybrane działanie to dodawanie")
    elif op_num == 2:
        logging.info("Wybrane działanie to odejmowanie")
    elif op_num == 3:
        logging.info("Wybrane działanie to mnożenie")
    elif op_num == 4:
        logging.info("Wybrane działanie to dzielenie")
    else:
        logging.info("Podana wartość jest nieprawidłowa")
        exit(1)
math_operation(op_num)

if op_num == 1:
    a = int(input('Podaj pierwszą liczbę: '))
    b = int(input(f'Podaj drugą liczbę: '))
    logging.info(f'Dodaję {a} i {b}')
    result = a + b
elif op_num == 2:
    a = int(input('Podaj pierwszą liczbę: '))
    b = int(input('Podaj drugą liczbę: '))
    logging.info(f'Odejmuję {a} i {b}')
    result = a - b
elif op_num == 3:
    a = int(input('Podaj pierwszą liczbę: '))
    logging.info(f'Pierwsza liczba to: {a}')
    b = int(input('Podaj drugą liczbę: '))
    logging.info(f'Druga liczba to: {b}')
    logging.info(f'Mnożę {a} i {b}')
    result = a * b
elif op_num == 4:
    a = int(input('Podaj pierwszą liczbę: '))
    b = int(input('Podaj drugą liczbę: '))
    logging.info(f'Dzielę {a} i {b}')
    result = a / b

if __name__ == "__main__":
    print(f'Wynik to: {result}')
