#Opracowanie: Kamila Kurowska, Marcin Brzeziński, Sylwester Brożyna, Tomasz Mielczarek
#WSPol w Szczytnie, II rok Informatyki
import time

#test złożoności liczby
def zlozonosc(a, d, n, s): 
    if pow(a, d, n) == 1:   #a**d mod n
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:  #a**(d*(2**i))
            return False
    return True 

#test pierwszości liczby
def pierwszosc(n, precyzja_dla_duzej_n = 16): #ustawienie precyzji, n-to liczba kolejnych liczb pierwszych, z którymi test zostanie wykonany
    if n in znane_liczby_pierwsze or n in (0, 1):
        return True 
    if any((n % p) == 0 for p in znane_liczby_pierwsze):
        return False    #oznacza, że liczba n jest podzielna przez znane_liczby_pierwsze
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    return not any(zlozonosc(a, d, n, s) for a in znane_liczby_pierwsze[:precyzja_dla_duzej_n])

znane_liczby_pierwsze = [2, 3]
znane_liczby_pierwsze += [x for x in range(5, 100000, 2) if pierwszosc(x)]
a=20    #losowo wybrana liczba a
liczby_pierwsze = []    #utworzenie pustej listy









