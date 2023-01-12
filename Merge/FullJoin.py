import pandas as pd

# Abrindo arquivo do Excel
loja1_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendedores_Join_Full_Loja1.xlsx', engine="openpyxl")

# Abrindo arquivo do Excel
loja2_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendedores_Join_Full_Loja2.xlsx', engine="openpyxl")

print("\n --------------------- Unindo os dataframes  --------------------- \n")

# Full join, unimos os arquivos, através do concat
vendasLoja1e2_DF = pd.concat([loja1_DF, loja2_DF])

print(vendasLoja1e2_DF)

#    Id Vendedor          Vendedor  Vendas    Meta
# 0        27264  Leonardo Almeida  5000.0     NaN
# 1        21732    Eliane Moreira  5000.0     NaN
# 2        27082   Nicolas Pereira  5000.0     NaN
# 3        22936    Amanda Martins  5000.0     NaN
# 4        21164      Paulo Santos  5000.0     NaN
# 5        28824   Gabriel Cardoso  5000.0     NaN
# 6        37579      Angela Maria  5000.0     NaN
# 7        20437    Carlos Moreira  5000.0     NaN
# 0        27265   Marcos Oliveira     NaN  5000.0
# 1        21732    Eliane Moreira     NaN  5000.0
# 2        27082   Nicolas Pereira     NaN  5000.0
# 3        22911     Pedro Camargo     NaN  5000.0

print("\n --------------------- Retirando Vendedores duplicados  --------------------- \n")

semClientesDuplicados_DF = vendasLoja1e2_DF.drop_duplicates(
    subset="Id Vendedor")

print(semClientesDuplicados_DF)

#    Id Vendedor          Vendedor  Vendas    Meta
# 0        27264  Leonardo Almeida  5000.0     NaN
# 1        21732    Eliane Moreira  5000.0     NaN
# 2        27082   Nicolas Pereira  5000.0     NaN
# 3        22936    Amanda Martins  5000.0     NaN
# 4        21164      Paulo Santos  5000.0     NaN
# 5        28824   Gabriel Cardoso  5000.0     NaN
# 6        37579      Angela Maria  5000.0     NaN
# 7        20437    Carlos Moreira  5000.0     NaN
# 0        27265   Marcos Oliveira     NaN  5000.0
# 3        22911     Pedro Camargo     NaN  5000.0
