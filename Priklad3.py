# Program 3: Číslo x patrí do intervalu a,b
a = float(input("Zadajte minimálnu hodnotu intervalu: "))
b = float(input("Zadajte maximálnu hodnotu intervalu: "))
x = float(input("Zadajte hodnotu x: "))
if a <= x <= b:
    print("Hodnota x sa nachádza v intervale.")
else:
    print("Hodnota x sa nenachádza v intervale.")   