import pandas as pd
import matplotlib.pyplot as plt

print('=' * 40)
dados = {'categoria':['A', 'B','C'],
        'total':[300, 180, 9940]}
df = pd.DataFrame(dados)
df.plot(kind='bar', x='categoria', y='total')
plt.show()