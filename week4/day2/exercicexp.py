# exercice1
my_fav_numbers = {"1","2"}
my_fav_numbers.add("3")
my_fav_numbers.add("4")
my_fav_numbers.pop()
friend_fav_numbers ={"8","16","6","0"}
our_fav_numbers =my_fav_numbers.union(friend_fav_numbers)


print(our_fav_numbers) 

#exercice2
# non on ne peut pas modifier un tuple donc on peut pas ajouter  plus d'entier.


# # exercice3
basket=["Banana","Apples","Oranges","Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Pommes")
len("Pommes")
basket.clear()
print(basket)

#  exercice4
s=1
for i in range (0,8):
     s=s+0.5
     print(s)

# exercice5
for i in range (1,21):
    print(i)

for i in range (1,21):
    if(i%2==0):
      print(i)

      #exercice6
name=''
while name!='larissa':
    name=input('what is your name?')
    
    # exercice7