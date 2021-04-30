# ==== Diferentes formas de criar dicionários com Python ===== #

contatos_one = {'Ale': '1234-5378', 'Pedro': '9999-9999'}
#{'Ale': '1234-5378', 'Pedro', '9999-9999'}

contatos_two = dict(Ale='1234-5378', Pedro='9999-9999')
#{'Ale': '1234-5378', 'Pedro', '9999-9999'}

contatos_lista = dict([('Mari', '1234-5678'), ('Pedro', '9999-9999'),
                    ('Ana', '8765-4321'), ('Barbara', '8877-7788')])
#{'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'Marina': '8877-7788'}

contatos_zip = dict(zip(['Ale', 'Pedro'], ['1234-5378', '9999-9999']))
#{'Ale': '1234-5378', 'Pedro', '9999-9999'}

print(contatos_lista)