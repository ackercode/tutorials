import cryptocompare 

btc = cryptocompare.get_price('BTC', currency='BRL')
print(btc)
# RESULTADO {'BTC': {'BRL': 314056.13}}

doge = cryptocompare.get_price('DOGE', currency='BRL')
print(doge)
# RESULTADO {'DOGE': {'BRL': 1.828}}