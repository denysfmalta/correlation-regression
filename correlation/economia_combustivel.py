import pandas as pd

# Lendo  a tabela do arquivo excel
df = pd.read_excel('dataset/regression.xls', sheet_name="economia_combustível")

# Calculando a correlação da tabela
correlation_matrix = df.corr()

# Imprimindo a correlação na tela
print(correlation_matrix)