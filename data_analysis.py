import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#caminhoframe fictício
caminho = rf"{os.environ.get('DATA_PATH')}"
print(f'Caminho do arquivo: {caminho}')

dado = pd.read_csv(caminho, sep=',', encoding='UTF-8')

# Gerando um gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(dado['x'], dado['y'], label='Dados')
plt.title('Gráfico de linha simples')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.legend()
plt.grid(True)
plt.show()
plt.bar(dado['x'], dado['y'], label='Dados')
plt.show()