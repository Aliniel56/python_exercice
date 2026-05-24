age = int(input("Quel est ton age ? "))
is_member_text = input("Es-tu membre ? ")
is_member = is_member_text.lower().strip() == "oui"

print(f"Tu as donc {age} ans")

if age >= 18:
    print("Tu es majeur !")
else:
    print("Tu es mineur !")

if age >= 18 and is_member:
    print("Accès autorisé")
else:
    print("Accès refusé")
