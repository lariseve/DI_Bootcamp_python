Matrix = [
    ["7","i","3"],
    ["T","s","i"],
    ["h","%","x"],
    ["i"," ", "#"],
    ["s","M"," "],
    ["$","a"," "],
    ["#","t","%"],
    ["^","r","!"]
]

def read(liste,index,*args):
    return liste[index]
chaine=[]
A = 0
while A < (len(Matrix[0])):
    cpt=0
    for line in Matrix :
        caract = read(line,A)
        if caract.isalpha() and caract !=" ":
            chaine.append(caract)
            cpt=0
        elif cpt==0:
            cpt+=1
            chaine.append("")
        elif cpt==1:
            chaine.append(" ")
            cpt+=1
    A +=1
print("".join(chaine))
