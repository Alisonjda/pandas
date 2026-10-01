# %%

import pandas as pd 

idades = {
    23,34,3,23,
    34,56,23,12,
    23,23,3,43,
}


series_idades = pd.Series(idades)
series_idades

# %% 
idades[0]
series_idades[0]
# %% 

# ordenar a serie com o "sort_values()"
series_idades = series_idades.sort_values()
series_idades

# %% 

# ".iloc[] faz olhar para a posição e não para o indici."
series_idades.iloc[0]
series_idades.iloc[-1]
# %%

idades = {
    23,34,3,23,
    34,56,23,12,
    23,23,3,43,
}


indexs = {
    "Alison","Teo","Lucas","Vinicios",
    "Ana","Marli","Luan","Maria",
    "João","Eduardo","Carlos","Rodolfo"
}
series_idades = pd.Series(idades, index=indexs)

series_idades["Ana"]

