# exercice1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
x = zip(keys,values)
print(dict (x))

# exercice2


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total=0
for x,y in family.items():
    if 0<=y<3:
        print(" the ticket is free for ",x)
        total=total+0
    elif 3<=y<=10:
        print(" the ticket is  10$ for ",x)
        total=total+10
    else:
        print(" the ticket is 15$for ",x)
        total=total+15
print(" the family’s total cost for the movies are",total)
families ={}
families= input("what is your name and ages")
print(families)


# exercise3
brand = {
   'name': 'Zara ',
'creation_date': 1975 ,
'creator_name': ['Amancio', 'Ortega',' Gaona' ],
'type_of_clothes': ['men', 'women', 'children', 'home' ],
'international_competitors': ['Gap', 'H&M', 'Benetton' ],
'number_stores':7000 ,
'major_color': {
    'France': 'blue', 
    'Spain':'red', 
   'US':['pink', 'green']

        }
        
}
brand.update({"number_stores": 2})
print("les clients de Zara sont:",brand['type_of_clothes']) 
brand['country_creation']='Spain'
if brand["international_competitors"]:
    brand["international_competitors"].append("Desigual")
    del(brand["creation_date"])
    print((brand['international_competitors'])[-1]) 
    print((brand['major_color'])['US'])
    print(len(brand.items()))
    print(brand.keys())
    more_on_Zara={
    'creation_date': 1975,
    'number_stores': 10000
}
    brand.update(more_on_Zara)
    print(brand["number_stores"])
    

# exercise4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A={users[i] :i for i in range (len(users)) }
print(disney_users_A)
disney_users_B={ i : users[i] for i in range (len(users)) }
print(disney_users_B)
disney_users_C = {}
for i, user in  enumerate(sorted(users)):
    disney_users_C[user] = i
print(disney_users_C)
disney_users_D={users[i]: i for i in range(len(users)) if "i" in users[i]}
print(disney_users_D)
disney_users_E={users[i]: i for i in range(len(users)) if users[i][0]=="M" or users[i][0]=="P"}
print(disney_users_E)