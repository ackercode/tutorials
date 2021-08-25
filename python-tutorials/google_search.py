# instalar a biblioteca - pip install google-search
from googlesearch import search

#Python será a palavra que vamos pesquisar
#num_results será o numero de resultados que será mostrado
#Em lang você pode definir a linguagem da busca

python_search = search("Python", num_results=10, lang="br")

#O print de python_search mostrará uma lista com os top 10 links

print(python_search)

#resultado
# ['https://www.python.org/', 'https://www.python.org/', 'https://en.wikipedia.org/wiki/Python_(programming_language)', 
# 'https://pt.wikipedia.org/wiki/Python', 'https://python.org.br/', 'https://www.codecademy.com/catalog/language/python', 
# 'https://www.udemy.com/topic/python/', 'https://pypi.org/']