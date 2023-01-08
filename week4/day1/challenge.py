# exercise1
severine = input("Saisir un mot de 10 caractere: ")
tail = len(severine)
if tail<10:
    print("la chaine n'est pas assez longue") 
if tail>10:
    print("la Chaine est trop longue")
if tail==10:
         print("la Chaine est trop longue")
for i in range(tail+1):
    print(severine[:+i])
