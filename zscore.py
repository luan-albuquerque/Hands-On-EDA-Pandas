import numpy as np
import pandas as pd

# Exemplo de dados
data = [10, 12, 13, 15, 12, 14, 100, 105, 110]  # 100+ são outliers
df = pd.DataFrame(data, columns=['valores'])

# Cálculo do z-score
media = df['valores'].mean()
desvio = df['valores'].std()

df['zscore'] = (df['valores'] - media) / desvio

# Filtrando outliers (|z| > 3)
outliers = df[np.abs(df['zscore']) > 3]

print("Média:", media)
print("Desvio-padrão:", desvio)
print("Outliers encontrados:\n", outliers)

