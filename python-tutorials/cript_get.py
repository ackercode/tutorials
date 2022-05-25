import cryptocompare

btc = cryptocompare.get_price('BTC', currency='BRL')
print(btc)

doge = cryptocompare.get_price('DOGE', currency='BRL')
print(doge)
