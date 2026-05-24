age = int(input("Quel est ton age ?"))
is_member = input("Es-tu membre ?")
print(f"Tu as donc {age} ans")
if age >= 18:
    print("Tu es majeur !")
else:
    print("Tu es mineur !")

if is_member == "oui":
    is_member = True
elif is_member == "Oui":
    is_member = True
else:
    is_member = False

if age >= 18 and is_member:
    print("Accès autorisé")
else:
    print("Accès refusé")
