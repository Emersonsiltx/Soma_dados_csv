import pandas as pd
tabela = pd.read_csv('air.csv', sep= ',')
print('A soma da coluna Tong é {} '.format(tabela['Tong'].sum()))
