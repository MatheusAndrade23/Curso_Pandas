import pandas as pd

# Abrindo arquivo do Excel
vendasLoja1_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Outer_Vendas_Loja1.xlsx', engine="openpyxl")

# Abrindo arquivo do Excel
vendasLoja2_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Outer_Vendas_Loja2.xlsx', engine="openpyxl")


print("\n Juntando dados com o outer e verificando os vendedores que venderam em ambas as lojas  \n")

verificandoVendas_DF = pd.merge(vendasLoja1_DF, vendasLoja2_DF, on=[
                                "Id Vendedor"], how="outer", suffixes=(" Loja 1", " Loja 2"))

print(verificandoVendas_DF)

#    Id Vendedor   Vendedor Loja 1  Vendas Loja 1  Vendedor Loja 2  Vendas Loja 2
# 0        27264  Leonardo Almeida         2627.0              NaN            NaN
# 1        21732    Eliane Moreira         2094.0              NaN            NaN
# 2        27082   Nicolas Pereira         4221.0  Nicolas Pereira         5000.0
# 3        22936    Amanda Martins         3993.0              NaN            NaN
# 4        21164      Paulo Santos         3202.0     Paulo Santos         3202.0
# 5        28824   Gabriel Cardoso         3889.0              NaN            NaN
# 6        37579      Angela Maria         3626.0              NaN            NaN
# 7        20437    Carlos Moreira         2103.0   Carlos Moreira         2103.0
# 8        27265               NaN            NaN  Marcos Oliveira         5000.0
# 9        22911               NaN            NaN    Pedro Camargo         5000.0

# dropna = Deleta as linhas que tem pelo menos 1 valor vazio


print("\n Removendo linhas com NaN \n")

tratandoDados_DF = verificandoVendas_DF.dropna()

print(tratandoDados_DF)

#    Id Vendedor  Vendedor Loja 1  Vendas Loja 1  Vendedor Loja 2  Vendas Loja 2
# 2        27082  Nicolas Pereira         4221.0  Nicolas Pereira         5000.0
# 4        21164     Paulo Santos         3202.0     Paulo Santos         3202.0
# 7        20437   Carlos Moreira         2103.0   Carlos Moreira         2103.0

print("\n Após remover coluna de Vendedor Loja 2 \n")

del tratandoDados_DF["Vendedor Loja 2"]

print(tratandoDados_DF)

#    Id Vendedor  Vendedor Loja 1  Vendas Loja 1  Vendas Loja 2
# 2        27082  Nicolas Pereira         4221.0         5000.0
# 4        21164     Paulo Santos         3202.0         3202.0
# 7        20437   Carlos Moreira         2103.0         2103.0
