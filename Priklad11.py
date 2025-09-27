# Program 11: Funkcia - najväčšie z troch čísel
def najvacsie(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(najvacsie(3, 7, 11))
print(najvacsie(200, 33, 998))