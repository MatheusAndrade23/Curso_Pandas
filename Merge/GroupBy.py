import pandas as pd

vendas_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Groupby.xlsx', engine="openpyxl")

print(vendas_DF)

print("\n --------------- groupby - Agrupas pela coluna de Vendedor e usando o mean para calcula a média ------------------\n")

#             Vendedor  Produto Data Venda  Preço  Qtd  Total Vendas
# 0   Leonardo Almeida  Laranja 2023-01-04   12.0    6          72.0
# 1     Eliane Moreira     Maça 2023-01-03    9.9    9          89.1
# 2    Nicolas Pereira  Laranja 2023-01-04   12.0    6          72.0
# 3     Amanda Martins  Laranja 2023-01-02   12.0    6          72.0
# 4       Paulo Santos  Abacate 2023-01-03   11.0   10         110.0
# 5    Gabriel Cardoso   Goiaba 2023-01-01    8.5    6          51.0
# 6   Leonardo Almeida  Laranja 2023-01-02   12.0    5          60.0
# 7     Eliane Moreira     Maça 2023-01-02    9.9    6          59.4
# 8    Nicolas Pereira  Laranja 2023-01-01   12.0    8          96.0
# 9     Amanda Martins  Laranja 2023-01-02   12.0    5          60.0
# 10               NaN  Laranja 2023-01-02   12.0    5          60.0
# 11               NaN  Laranja 2023-01-01   12.0    9         108.0
# 12               NaN   Banana 2023-01-03    6.9    5          34.5
# 13               NaN  Abacate 2023-01-03   11.0   10         110.0
# 14               NaN   Goiaba 2023-01-01    8.5    7          59.5
# 15               NaN     Maça 2023-01-03    9.9    6          59.4
# 16               NaN     Maça 2023-01-03    9.9   10          99.0
# 17               NaN  Laranja 2023-01-04   12.0    7          84.0
# 18               NaN  Abacate 2023-01-03   11.0    5          55.0
# 19               NaN   Goiaba 2023-01-04    8.5    8          68.0
# 20   Gabriel Cardoso  Abacate 2023-01-04   11.0    6          66.0
# 21  Leonardo Almeida  Laranja 2023-01-01   12.0   10         120.0
# 22    Eliane Moreira     Maça 2023-01-04    9.9   10          99.0
# 23   Nicolas Pereira  Laranja 2023-01-03   12.0    8          96.0
# 24    Amanda Martins  Laranja 2023-01-01   12.0    9         108.0
# 25    Eliane Moreira  Abacate 2023-01-02   11.0    8          88.0
# 26   Nicolas Pereira   Goiaba 2023-01-04    8.5    7          59.5
# 27    Amanda Martins  Laranja 2023-01-04   12.0    9         108.0

# groupby - Agrupas pela coluna de Vendedor e usando o mean para calcula a média
mediaVendedor = vendas_DF.groupby(["Vendedor"]).mean()

print(mediaVendedor)

#                    Preço    Qtd  Total Vendas
# Vendedor
# Amanda Martins    12.000   7.25        87.000
# Eliane Moreira    10.175   8.25        83.875
# Gabriel Cardoso    9.750   6.00        58.500
# Leonardo Almeida  12.000   7.00        84.000
# Nicolas Pereira   11.125   7.25        80.875
# Paulo Santos      11.000  10.00       110.000

print("\n --------------- groupby - Agrupa pela coluna de Vendedor e usa o sum para calcular a soma ------------------\n")

somaVendedor = vendas_DF.groupby(["Vendedor"]).sum()

print(somaVendedor)

#                   Preço  Qtd  Total Vendas
# Vendedor
# Amanda Martins     48.0   29         348.0
# Eliane Moreira     40.7   33         335.5
# Gabriel Cardoso    19.5   12         117.0
# Leonardo Almeida   36.0   21         252.0
# Nicolas Pereira    44.5   29         323.5
# Paulo Santos       11.0   10         110.0

print("\n --------------- Agrupa pela coluna vendedor e considera valores em branco --------------- \n")

# groupby = Agrupa pela coluna
# dropna = deleta as linhas que tem pelo menos um valor em branco
# by = usar a coluna como critério para fazer o groupby
# sum = soma
deixandoValoresEmBranco = vendas_DF.groupby(
    by=["Vendedor"], dropna=False).sum()

print(deixandoValoresEmBranco)

#                   Preço  Qtd  Total Vendas
# Vendedor
# Amanda Martins     48.0   29         348.0
# Eliane Moreira     40.7   33         335.5
# Gabriel Cardoso    19.5   12         117.0
# Leonardo Almeida   36.0   21         252.0
# Nicolas Pereira    44.5   29         323.5
# Paulo Santos       11.0   10         110.0
# NaN               101.7   72         737.4

print("\n --------------- Agrupa pela coluna vendedor e remove valores em branco ---------------\n")

removendoValoresEmBranco = vendas_DF.groupby(
    by=["Vendedor"], dropna=True).sum()

print(removendoValoresEmBranco)

# Vendedor
# Amanda Martins     48.0   29         348.0
# Eliane Moreira     40.7   33         335.5
# Gabriel Cardoso    19.5   12         117.0
# Leonardo Almeida   36.0   21         252.0
# Nicolas Pereira    44.5   29         323.5
# Paulo Santos       11.0   10         110.0

print("\n --------------- Agrupa pelas colunas de Vendedor e Produto e faz uma soma dos valores --------------- \n")

agrupaDuasColunas = vendas_DF.groupby(["Vendedor", "Produto"]).sum()

print(agrupaDuasColunas)

#                           Preço  Qtd  Total Vendas
# Vendedor         Produto
# Amanda Martins   Laranja   48.0   29         348.0
# Eliane Moreira   Abacate   11.0    8          88.0
#                  Maça      29.7   25         247.5
# Gabriel Cardoso  Abacate   11.0    6          66.0
#                  Goiaba     8.5    6          51.0
# Leonardo Almeida Laranja   36.0   21         252.0
# Nicolas Pereira  Goiaba     8.5    7          59.5
#                  Laranja   36.0   22         264.0
# Paulo Santos     Abacate   11.0   10         110.0

print("\n --------------- Agrupa pelas colunas de Data Venda e Vendedor e faz uma soma dos valores --------------- \n")

agrupaDataVendedor = vendas_DF.groupby(["Data Venda", "Vendedor"]).sum()

print(agrupaDataVendedor)

# Data Venda Vendedor
# 2023-01-01 Amanda Martins     12.0    9         108.0
#            Gabriel Cardoso     8.5    6          51.0
#            Leonardo Almeida   12.0   10         120.0
#            Nicolas Pereira    12.0    8          96.0
# 2023-01-02 Amanda Martins     24.0   11         132.0
#            Eliane Moreira     20.9   14         147.4
#            Leonardo Almeida   12.0    5          60.0
# 2023-01-03 Eliane Moreira      9.9    9          89.1
#            Nicolas Pereira    12.0    8          96.0
#            Paulo Santos       11.0   10         110.0
# 2023-01-04 Amanda Martins     12.0    9         108.0
#            Eliane Moreira      9.9   10          99.0
#            Gabriel Cardoso    11.0    6          66.0
#            Leonardo Almeida   12.0    6          72.0
#            Nicolas Pereira    20.5   13         131.5
