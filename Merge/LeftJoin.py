import pandas as pd

# PROCV - Vem do Excel, procurar uma informação de outra tabela

# Abrindo arquivo do Excel
vendas_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendas_LEFT_JOIN.xlsx', engine="openpyxl")

print(vendas_DF)

#    Id Vendedor          Vendedor  Vendas
# 0        27264  Leonardo Almeida    4144
# 1        21732    Eliane Moreira    7985
# 2        27082   Nicolas Pereira    7892
# 3        22936    Amanda Martins    5469
# 4        21164      Paulo Santos    6572
# 5        28824   Gabriel Cardoso    6140
# 6        37579      Angela Maria    5003
# 7        20437    Carlos Moreira    6799

# Abrindo arquivo do Excel
vendedores_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendedores_LEFT_JOIN.xlsx', engine="openpyxl")

print(vendedores_DF)

#    Id Vendedor        Vendedor
# 0        22936  Amanda Martins
# 1        37579    Angela Maria
# 2        20437  Carlos Moreira

print("\n --------------------- vendedores comuns --------------------- \n")

verificandoVendas_DF = pd.merge(
    vendas_DF, vendedores_DF, on="Id Vendedor", how="left")

print(verificandoVendas_DF)

#    Id Vendedor        Vendedor_x  Vendas      Vendedor_y
# 0        27264  Leonardo Almeida    4144             NaN
# 1        21732    Eliane Moreira    7985             NaN
# 2        27082   Nicolas Pereira    7892             NaN
# 3        22936    Amanda Martins    5469  Amanda Martins
# 4        21164      Paulo Santos    6572             NaN
# 5        28824   Gabriel Cardoso    6140             NaN
# 6        37579      Angela Maria    5003    Angela Maria
# 7        20437    Carlos Moreira    6799  Carlos Moreira

print("\n --------------------- vendedores comuns --------------------- \n")

verificandoVendas_DF_2 = pd.merge(
    vendas_DF, vendedores_DF, on="Id Vendedor", how="left", suffixes=(" Vendas", " Checagem"))


print(verificandoVendas_DF_2)

#    Id Vendedor   Vendedor Vendas  Vendas Vendedor Checagem
# 0        27264  Leonardo Almeida    4144               NaN
# 1        21732    Eliane Moreira    7985               NaN
# 2        27082   Nicolas Pereira    7892               NaN
# 3        22936    Amanda Martins    5469    Amanda Martins
# 4        21164      Paulo Santos    6572               NaN
# 5        28824   Gabriel Cardoso    6140               NaN
# 6        37579      Angela Maria    5003      Angela Maria
# 7        20437    Carlos Moreira    6799    Carlos Moreira

print("\n --------------------- Tratando as planinhas --------------------- \n")

# deletando as linhas que possuem pelo menos 1 nan
tratandoDataFrame = verificandoVendas_DF_2.dropna()

print("\n --------------------- Deletando coluna --------------------- \n")

del tratandoDataFrame["Vendedor Checagem"]
