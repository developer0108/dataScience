import pandas

ais = pandas.read_csv('./data/ais.csv')
ais.set_index('id')
print(ais.info())