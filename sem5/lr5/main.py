from currencies import CurrenciesLst

c = CurrenciesLst()
c.select_valute('R01010')
c.select_valute('R01035')
c.select_valute('R01235')
ci = c.get_currencies()
aud = c['AUD']
usd = c['USD']
# print(ci)
print(aud)
print(usd)

t = c.get_last_update()
print(t)

c.visualize_currencies()