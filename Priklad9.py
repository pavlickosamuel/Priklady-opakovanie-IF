# Program 9: Kontrola písmena v reťazci
a = (input("Zadaj retazec: "))
b = (input("Zadaj pismeno: "))
print(b in a)
if b in a:
    print ("Pismeno sa nachadza v retazci")
else:
    print ("Pismeno sa nenachadza v retazci")