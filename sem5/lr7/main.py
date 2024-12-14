from currencies import CurrenciesDecoratorCSV, CurrenciesLst, CurrenciesDecoratorJSON

c1 = CurrenciesLst()
c1.select_valute('R01010')
c1.select_valute('R01035')
c1.select_valute('R01235')
ci = c1.get_currencies()
aud = c1['AUD']
usd = c1['USD']
# print(ci)
print(aud)
print(usd)

# c1.visualize_currencies()

t1 = c1.get_last_update()
c2 = CurrenciesLst()
t2 = c2.get_last_update()
print(t1, t2)
print(t1 == t2)

# c_dec = CurrenciesDecorator(c1)

c_json = CurrenciesDecoratorJSON(c1)
j = c_json.get_currencies()
print(j)

c_csv = CurrenciesDecoratorCSV(c1)
csv = c_csv.get_currencies()
print(csv)