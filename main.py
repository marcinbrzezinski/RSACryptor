from random import randrange, random, choice
import MillerRabin, Banners, csv

'''
Generowanie listy zawierającej liczby pierwsze z podanego zakresu
'''

def prime_generator():
    for liczba in range(100001, 120003, 2):   #zakres jaki chcemy przeszukać - tylko liczby nieparzyste
        if MillerRabin.pierwszosc(liczba):
            MillerRabin.liczby_pierwsze.append(liczba)
    if len(MillerRabin.liczby_pierwsze) == 0:
        raise AssertionError("Nie znaleziono liczby pierwszej w podanym zakresie")
    return MillerRabin.liczby_pierwsze




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




def wybierz_e(fi):
    while True:
        e = randrange(2, fi)
        if (nwd(e, fi)) == 1:
            return e



def keygen():
    prime_list = prime_generator()
    '''
    Wybieranie p i q
    '''
    p = choice(prime_list)
    prime_list.remove(p)
    q = choice(prime_list)

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
    e = wybierz_e(fi_n)

    '''
    Znajdujemy liczbę d, gdzie jej różnica z odwrotnością modularną liczby e jest podzielna przez fi_n
    '''

    gcd, x, y = xgcd(e, fi_n)
    if (x < 0):
        d = x + fi_n
    else:
        d = x

    # print('Sprawdzenie czy (e * d) % fi_n = 1. Wynik: ', (e * d) % fi_n)

    '''
    Klucz publiczny jest definiowany jako para licb (n, e), natomiast kluczem prywatnym jest para (n, d)
    '''

    public_key = (str(n) + '\n' + str(e) + '\n')
    private_key = (str(n) + '\n' + str(d) + '\n')

    # print('Klucz publiczny: \n', public_key)
    #     # print('Klucz prywatny: \n', private_key)
    #     #
    #     # print(f'Priv = {str(n) + str(d)}')
    #     # print(f'Pub = {str(n) + str(e)}')
    return n, e, d


'''
Funkcja szyfrujaca
'''

def encrypt(msg):
    return pow(msg, e, n)

'''
Funkcja deszyfrująca
'''
def decrypt(msg):
    return pow(msg, d, n)


def convertIntList(list):
    s = [str(i) for i in list]

    res = int("".join(s))

    return res

'''
Pętla zamieniająca znaki ze string'a na liczby dziesiętne
'''
def strToAscii(string):
    lista_ascii = []  # Lista z liczbami dziesiętnymi

    for i in string:
        lista_ascii.append(ord(i))
    return lista_ascii
"""
Pętla zamieniająca kody ASCII na string
"""
def asciiToString(asci):
    lista_string = []

    for i in asci:
        lista_string.append(chr(i))
    return lista_string

def zapiszDoCsv(x, filename, tryb):
    filenamecsv = filename + ".csv"

    with open(filenamecsv, tryb, encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([x])

def wczytajKlucz(filename):
    filenamecsv = filename + ".csv"
    reader = csv.reader(
        open(filenamecsv, 'r'),
            quoting=csv.QUOTE_NONE
    )
    p1 = next(reader)
    p2 = next(reader)
    return int(p1[0]), int(p2[0])

if __name__ == '__main__':
    n, e = wczytajKlucz('pubkey')
    n, d = wczytajKlucz('privkey')
    wybor=None
    # print(prime_generator())
    while wybor != 0:
        Banners.bannerMain()
        print(type(n))
        print(f'Klucz publiczny: e = {n}, n = {e}')
        print(f'Klucz prywatny: e = {n}, n = {d}')
        wybor = int(input("Wybierz od 0 do 3: "))
        if wybor == 1:
            n, e, d = keygen()
            zapiszDoCsv(n, 'pubkey', 'w')
            zapiszDoCsv(e, 'pubkey', 'a')
            zapiszDoCsv(n, 'privkey', 'w')
            zapiszDoCsv(d, 'privkey', 'a')
        elif wybor == 2:
            Banners.bannerZaszyfruj()
            msg = input('Wpisz wiadomość:\n')
            asci_list = strToAscii(msg)
            print('Asci list: ', asci_list)
            bigInt = convertIntList(asci_list)
            encrypted_msg = encrypt(bigInt)
            print(encrypted_msg)
            # encrypted_str = ''.join(str(i) for i in encrypted_msg)
            # print(encrypted_str)
        elif wybor == 3:
            Banners.bannerOdszyfruj()
            msg = input('Wpisz wiadomość:\n')
            decrypted_int = decrypt(int(msg))
            decrypted_str = str(decrypted_int)
            decrypted_msg = [decrypted_str[i:i+3] for i in range(0, len(decrypted_str), 3)]
            print(decrypted_msg)
            decrypted_msg_to_int =  list(map(int, decrypted_msg))
            char_list = asciiToString(decrypted_msg_to_int)
            # decrypted_msg = decrypt(asci_list)
            decrypted_str = ''.join(char_list)
            print(decrypted_str)
        else:
            pass
    exit()