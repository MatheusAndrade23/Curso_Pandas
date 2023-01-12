import pandas as pd

# Pivot - Está função não suporta agregação de valores repetidos

baseLanchonete_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendas_Lanchonete_Pivot.xlsx', engine="openpyxl")

print("\n --------------- Imprimindo clientes / Preço com Desconto ------------------\n")

print(baseLanchonete_DF)

#   Data Venda          Cliente     Produto  Preço Total  Preço com Desconto
# 0 2023-01-04     Angela Maria        Café            4                 3.8
# 1 2023-01-03   Carlos Moreira  Salgadinho            9                 8.0
# 2 2023-01-04  Gabriel Cardoso        Coca            8                 6.0
# 3 2023-01-01     Paulo Santos      Pastel           10                 5.0
# 4 2023-01-01    Rosiane Silas        Coca            8                 6.0

# index = linhas
# columns = As colunas
pivotExemplo1 = baseLanchonete_DF.pivot(
    index="Data Venda", columns="Cliente", values="Preço com Desconto")

print(pivotExemplo1)

# Cliente     Angela Maria  Carlos Moreira  Gabriel Cardoso  Paulo Santos  Rosiane Silas
# Data Venda
# 2023-01-01           NaN             NaN              NaN           5.0            6.0
# 2023-01-03           NaN             8.0              NaN           NaN            NaN
# 2023-01-04           3.8             NaN              6.0           NaN            NaN


print("\n --------------- Imprimindo clientes / Preço com Desconto ------------------\n")

# index = linhas
# columns = As colunas
pivotExemplo2 = baseLanchonete_DF.pivot(
    index="Cliente", columns="Data Venda", values="Preço com Desconto")

print(pivotExemplo2)

# Data Venda       2023-01-01  2023-01-03  2023-01-04
# Cliente
# Angela Maria            NaN         NaN         3.8
# Carlos Moreira          NaN         8.0         NaN
# Gabriel Cardoso         NaN         NaN         6.0
# Paulo Santos            5.0         NaN         NaN
# Rosiane Silas           6.0         NaN         NaN
