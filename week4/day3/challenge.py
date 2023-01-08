# exercise1
def create_dictionary(word):
   letter_dict = {}
  
   for i, letter in enumerate(word):
     if letter in letter_dict:
       letter_dict[letter].append(i) 
     else:
       letter_dict[letter] = [i]
  
   return letter_dict

word = input("Saisir un mot:")

letter_dict = create_dictionary(word)

print(letter_dict)

# exercise2

def articles_magasin(argent, articles, prix):
  achats_possibles = []
  for i in range(len(articles)):
    if argent >= prix[i]:
      achats_possibles.append(articles[i])
  if not achats_possibles:
    return "Rien"
  achats_possibles.sort()
  return achats_possibles

argent = 20
articles = ["pomme", "banane", "orange", "kiwi"]
prix = [1, 2, 3, 4]
print(articles_magasin(argent, articles, prix)) 

