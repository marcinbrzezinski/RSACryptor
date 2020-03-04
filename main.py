from random import randrange

'''
Generowanie liczb pierwszych
'''


def prime_generator():
    return 0


'''
Dla testów lczby pierwsze podane na sztywno
'''
p = 30133
q = 99767

'''
Sprawdzanie pierwszości
'''


def czy_pierwsza(liczba):
    if liczba == 2:
        return True
    if liczba < 2 or liczba % 2 == 0:
        return False
    for n in range(3, int(liczba ** 0.5) + 2, 2):
        if liczba % n == 0:
            return False
    return True


'''
Algorytm Euklidesa
'''


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


'''
Rozszerzony algorytm Euklidesa 
'''


def xgcd(a, b):
    x, ox = 0, 1
    y, oy = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        ox, x = x, ox - quotient * x
        oy, y = y, oy - quotient * y
    return a, ox, oy


'''
Obliczamy 'n'
'''
n = p * q

'''
Obiczamy wartość funkcji Eulera
'''
fi_n = (p - 1) * (q - 1)

'''
Wybieramy liczbę 'e' spełniającą warunek: 
1 < e < fi_n
'''


def wybierz_e(fi):
    while True:
        e = randrange(2, fi)
        if (nwd(e, fi)) == 1:
            return e


e = wybierz_e(fi_n)
'''
Znajdujemy liczbę d, gdzie jej różnica z odwrotnością modularną liczby e jest podzielna przez fi_n
'''

gcd, x, y = xgcd(e, fi_n)
if(x < 0):
    d = x + fi_n
else:
    d = x

print('Sprawdzenie czy (e * d) % fi_n = 1. Wynik: ', (e*d)%fi_n)


'''
Klucz publiczny jest definiowany jako para licb (n, e), natomiast kluczem prywatnym jest para (n, d)
'''

public_key = (str(n) + '\n' + str(e) + '\n')
private_key = (str(n) + '\n' + str(d) + '\n')

print('Klucz publiczny: \n', public_key)
print('Klucz prywatny: \n', private_key)