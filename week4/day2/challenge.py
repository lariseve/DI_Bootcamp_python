# challenge1
a = int(input("entrez un nombre:"))
b = int(input("entrez une taille:"))
multiple = 0
lis = []
while b>0:
 	multiple = a + multiple
lis.append(multiple)
b = b - 1 
print(lis)

# challenge2
Chaine = input(" saisissez une phrase : ")
chaine = ""
for i in Chaine:
    if i not in chaine:
        chaine += i
print(f"{Chaine}")
print(f"la nouvelle chaine {chaine}")
