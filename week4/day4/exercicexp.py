#  # exercise1
def display_message():
    print("dans cette formation nous apprenons beaucoup de chose en python ,django")
display_message()


# # exercise2
def favorite_book(title):
  print(f"One of my favorite books is {title}")
favorite_book("la chevre de ma mere  ")

# # exercise3
def describe_city(city,country = "Burkina Faso") :
     print(f"{city} est en {country}")
describe_city("Ouagadougou")

# exercise4
import random
from random import randint
def randomNumber(i):
  randomNumb = random.randint(1, 100)
  if i== randomNumb:
    print("Succès!!!")
  else:
    print("échec")
    print("le nombre", i)
    print("le nombre aléatoire ",randomNumb)
randomNumber(27)

# exercise5
def make_shirt(size="l", text="J'aime Python"):
  print(f"The size of the shirt is {size} and the text is {text}")
make_shirt()
make_shirt(size="xxl", text="J'aime Python")
make_shirt(size="M ", text="J'aime Python")
make_shirt(size="xl", text="J'aime Python")

# exercise6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names) :
      for i in range(len(magician_names)):
        print(magician_names[i])
list(filter(lambda a: print(a),magician_names))

def make_great(liste) :
    for i in range(0,len(liste)):
        liste[i] += " the Great"
make_great(magician_names)
show_magicians(magician_names)

# exercise7
def get_random_temp(saison) :
    import random
    if saison == "hiver" :
        return random.randint(-10, 16)
    elif saison == "été" :
        return random.randint(10, 25)
    elif saison == "printemps" :
        return random.randint(0, 15)
    elif saison == "automne" :
        return random.randint(20, 40)
    else :
        print("c'est pas une saison")
        return 0
    
def main() :
    temps = get_random_temp(input("Saisissez une saison : "))
    print(f"la temperature actuelle est de {temps} dégré celsus ")
    if temps < 0 :
        print("chic saison")
    elif temps < 16 :
        print("temps unp bizarre")
    elif temps <= 23 :
        print("portez un pull en sortant")
    elif temps < 32 :
        print("waouhh chiccc vous pouvez sortir tranquille")
    elif temps < 40 :
        print("ayyyaya attention!!")
    else:
        print("c'est pas une saison")

main()