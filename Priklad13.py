import math

def korene_kvadratickej(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Rovnica má nekonečne veľa riešení"
            else:
                return "Rovnica nemá riešenie"
        else:
            x = -c / b
            return f"Lineárna rovnica, riešenie je x = {x}"

    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return f"Rovnica má dva reálne korene: x1 = {x1} x2 = {x2}"
    
    elif D == 0:
        x3 = -b / (2*a)
        return f"Rovnica má jeden reálny koreň: x = {x3}"
    else:
        return "Rovnica nemá reálne korene"
print(korene_kvadratickej(1, -3, 2))
print(korene_kvadratickej(1, 2, 1)) 
print(korene_kvadratickej(1, 0, 1)) 