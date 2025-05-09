import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
column_names = [
    "Sexo", "Longitud", "Diametro", "Altura", "pesoEntero",
    "PesoDesconchado", "PesoViscera", "PesoConcha", "Anillos"]

df = pd.read_csv(url, header=None, names=column_names)
print(df.head())

#mostrar las primeras filas y estructuras
print("Primeras filas")
print(df.head())
print("\nInformación del dataset:")+

print(df.info())
print("\nEstadísticas descriptivas:")
print(df.describe(include="all"))

#verificar duplicados
