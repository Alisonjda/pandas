import pandas as pd 

idades = {
    23,34,3,23,
    34,56,23,12,
    23,23,3,43,
}


nomes = {
    "Alison","Teo","Lucas","Vinicios",
    "Ana","Marli","Luan","Maria",
    "João","Eduardo","Carlos","Rodolfo"
}

series_idades = pd.Series(idades)
series_nome = pd.Series(nomes)