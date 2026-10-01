# %% 

idades = {
    23,34,3,23,
    34,56,23,12,
    23,23,3,43,
}

media = sum(idades) / len(idades)
print("media", media)

diffs = 0
for i in idades:
    diffs += (1-media) **2

    variancia = diffs / (len(idades)-1)

print("variancia: ", variancia )  

# %%

import pandas as pd 

idades = {
    23,34,3,23,
    34,56,23,12,
    23,23,3,43,
}

# armazenando dados em Series.
series_idades = pd.Series(idades)
series_idades

# %% 
# estatisticas da séries

# com o "mean()" calcula a media.
media_idades = series_idades.mean()

#calcula a variança com "var()"
var_idades = series_idades.var()

#descreve tudo com "describe()"
summary_idades = series_idades.describe()
summary_idades