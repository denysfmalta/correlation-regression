import pandas as pd

df = pd.read_excel('dataset/regression.xls', sheet_name="consumo")

correlation_matrix = df.corr()

print(correlation_matrix)
