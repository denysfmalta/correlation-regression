import pandas as pd
import numpy as np

df = pd.read_excel('dataset/regression.xls', sheet_name="economia_combustível")

X1 = df['Cylinders (x1)']
X2 = df['Deslocamento (x2)']
y = df['CityMPG (y)']
X = np.column_stack((X1, X2))
model = np.linalg.lstsq(X, y, rcond=None)[0]
coef_x1, coef_x2 = model
print(f"Coeficiente para X1: {coef_x1}")
print(f"Coeficiente para X2: {coef_x2}")
