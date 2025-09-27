# Program 12: Funkcia trojuholník
def je_trojuholnik(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            return "Je to trojuholnik - pravouhly"
        elif a == b == c:
            return "Je to trojuholnik - rovnostranny"
        elif (a == b and a != c) or (a == c and b != c) or (b == c and a != c):
            return "Je to trojuholnik - rovnoramenny"
        else:
            return "Je to trojuholnik"
    else:
        return "Nie je to trojuholnik"
print(je_trojuholnik(3, 4, 5))
print(je_trojuholnik(2, 2, 2))