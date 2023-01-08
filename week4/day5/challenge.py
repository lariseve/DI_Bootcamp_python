phrase= input('saisissez uniquement des mots separés par des virgules : ')
phrase = phrase.split(',')
sequence = sorted(phrase)
phrase1=""
for x in phrase:
    phrase1 += x + ','
print(phrase1)
