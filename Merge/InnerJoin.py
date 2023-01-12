import pandas as pd

# Abrindo arquivo do Excel
loja1_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendas_+INNER_JOIN_Loja1.xlsx', engine="openpyxl")

# Abrindo arquivo do Excel
loja2_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendas_+INNER_JOIN_Loja2.xlsx', engine="openpyxl")

print("\n --------------------- Inner Join de vendedores --------------------- \n")

# USAR MERGE COM ALGO QUE NÃO SE REPETE NA TABELA

# on -> indica a coluna
# -> inner gera um novo dataframe com o que há em comum entre 2 dataframes ou mais
# -> como
vendedoresEmComum = pd.merge(loja1_DF, loja2_DF, on=["Vendedor"], how="inner")

print(vendedoresEmComum)

# X = Loja 1, Y = Loja 2

#          Vendedor              Produto_x Data Venda_x  Quantidade Vendida_x  ...  Data Venda_y  Quantidade Vendida_y Valor Unitário_y Total Vendas_y
# 0  Amanda Martins       Vestido Infantil   2023-01-10                     1  ...    2023-02-04                     3           148.56         445.68
# 1  Carlos Moreira  Calça Feminina Jogger   2023-01-17                     7  ...    2023-02-17                    10            69.99         699.90

# Exibiu o nome de todas as colunas
print(vendedoresEmComum.columns.values)

# [2 rows x 11 columns]
# ['Vendedor' 'Produto_x' 'Data Venda_x' 'Quantidade Vendida_x'
#  'Valor Unitário_x' 'Total Vendas_x' 'Produto_y' 'Data Venda_y'
#  'Quantidade Vendida_y' 'Valor Unitário_y' 'Total Vendas_y']

print("\n --------------------- Vendas Lojas, resumo --------------------- \n")

# suffixes = nome das colunas
vendedoresEmComumResumo = pd.merge(
    loja1_DF, loja2_DF[["Vendedor", "Total Vendas"]], on=["Vendedor"], how="inner", suffixes=(" Loja 1", " Loja 2"))

print(vendedoresEmComumResumo)

#          Vendedor                Produto Data Venda  Quantidade Vendida  Valor Unitário  Total Vendas Loja 1  Total Vendas Loja 2
# 0  Amanda Martins       Vestido Infantil 2023-01-10                   1           59.90               59.90              445.68
# 1  Carlos Moreira  Calça Feminina Jogger 2023-01-17                   7           69.99              489.93              699.90

print("\n --------------------- Vendas Lojas, resumo 2--------------------- \n")

# suffixes = nome das colunas
vendedoresEmComumResumo2 = vendedoresEmComumResumo[[
    "Vendedor", "Total Vendas Loja 1", "Total Vendas Loja 2"]]

print(vendedoresEmComumResumo2)

# --------------------- Vendas Lojas, resumo 2---------------------

#          Vendedor  Total Vendas Loja 1  Total Vendas Loja 2
# 0  Amanda Martins                59.90               445.68
# 1  Carlos Moreira               489.93               699.90
