#Contando itens em uma lista =) 
#com Counter

from collections import Counter

minhas_lista = [10, 10, 5, 2, 9, 9, 9, 8]
contar = Counter(minhas_lista)

print(contar)
print(contar[9])
print(contar.most_common(1))
