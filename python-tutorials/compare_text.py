import filecmp

filecmp.cmp('arquivo1.txt', 'arquivo2.txt')
# Resultado >> True

filecmp.cmp('arquivo1.txt', 'arquivo3.txt')
# Resultado >> False