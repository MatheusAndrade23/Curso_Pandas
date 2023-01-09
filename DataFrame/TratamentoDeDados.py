import pandas as pd

# Abrindo arquivo do Excel
dados_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Tratamento_Dados.xlsx', engine="openpyxl")

print(dados_DF)

#             Vendedor Data Venda  Total Vendas
# 0     Amanda Martins 2023-01-01         751.0
# 1     Amanda Martins 2023-01-02         988.0
# 2     Eliane Moreira 2023-01-03         688.0
# 3     Eliane Moreira 2023-01-04         255.0
# 4    Gabriel Cardoso 2023-01-05         281.0
# 5    Gabriel Cardoso 2023-01-06         381.0
# 6    Ismael Silveira 2023-01-07         273.0
# 7    Ismael Silveira 2023-01-08         932.0
# 8    Ismael Silveira 2023-01-09         381.0
# 9   Leonardo Almeida 2023-01-10         479.0
# 10  Leonardo Almeida 2023-01-11         469.0
# 11   Nicolas Pereira 2023-01-12         502.0
# 12   Nicolas Pereira 2023-01-13           NaN
# 13      Paulo Santos 2023-01-14           NaN
# 14      Paulo Santos 2023-01-15           NaN
# 15   Rodolfo Martins 2023-01-02           NaN
# 16   Rodolfo Martins 2023-01-03           NaN
# 17   Rodolfo Martins 2023-01-04           NaN
# 18     Rodrigo Pires 2023-01-05           NaN
# 19     Rodrigo Pires 2023-01-06           NaN
# 20     Rodrigo Pires 2023-01-07           NaN

print("\n --------------------- Preenchendo os valores vazios com valores padrão --------------------- \n")

# dados_DF['Total Vendas'] = dados_DF['Total Vendas'].fillna(3)

# print(dados_DF)

#             Vendedor Data Venda  Total Vendas
# 0     Amanda Martins 2023-01-01         751.0
# 1     Amanda Martins 2023-01-02         988.0
# 2     Eliane Moreira 2023-01-03         688.0
# 3     Eliane Moreira 2023-01-04         255.0
# 4    Gabriel Cardoso 2023-01-05         281.0
# 5    Gabriel Cardoso 2023-01-06         381.0
# 6    Ismael Silveira 2023-01-07         273.0
# 7    Ismael Silveira 2023-01-08         932.0
# 8    Ismael Silveira 2023-01-09         381.0
# 9   Leonardo Almeida 2023-01-10         479.0
# 10  Leonardo Almeida 2023-01-11         469.0
# 11   Nicolas Pereira 2023-01-12         502.0
# 12   Nicolas Pereira 2023-01-13           3.0
# 13      Paulo Santos 2023-01-14           3.0
# 14      Paulo Santos 2023-01-15           3.0
# 15   Rodolfo Martins 2023-01-02           3.0
# 16   Rodolfo Martins 2023-01-03           3.0
# 17   Rodolfo Martins 2023-01-04           3.0
# 18     Rodrigo Pires 2023-01-05           3.0
# 19     Rodrigo Pires 2023-01-06           3.0
# 20     Rodrigo Pires 2023-01-07           3.0

print("\n --------------------- Preenchendo os valores vazios com a média de vendas --------------------- \n")

# fillna preenche os valores vazios
# mean calcula a média
# dados_DF['Total Vendas'] = dados_DF['Total Vendas'].fillna(
#     dados_DF['Total Vendas'].mean())

# print(dados_DF)

#             Vendedor Data Venda  Total Vendas
# 0     Amanda Martins 2023-01-01    751.000000
# 1     Amanda Martins 2023-01-02    988.000000
# 2     Eliane Moreira 2023-01-03    688.000000
# 3     Eliane Moreira 2023-01-04    255.000000
# 4    Gabriel Cardoso 2023-01-05    281.000000
# 5    Gabriel Cardoso 2023-01-06    381.000000
# 6    Ismael Silveira 2023-01-07    273.000000
# 7    Ismael Silveira 2023-01-08    932.000000
# 8    Ismael Silveira 2023-01-09    381.000000
# 9   Leonardo Almeida 2023-01-10    479.000000
# 10  Leonardo Almeida 2023-01-11    469.000000
# 11   Nicolas Pereira 2023-01-12    502.000000
# 12   Nicolas Pereira 2023-01-13    531.666667
# 13      Paulo Santos 2023-01-14    531.666667
# 14      Paulo Santos 2023-01-15    531.666667
# 15   Rodolfo Martins 2023-01-02    531.666667
# 16   Rodolfo Martins 2023-01-03    531.666667
# 17   Rodolfo Martins 2023-01-04    531.666667
# 18     Rodrigo Pires 2023-01-05    531.666667
# 19     Rodrigo Pires 2023-01-06    531.666667
# 20     Rodrigo Pires 2023-01-07    531.666667

print("\n --------------------- Preenchendo os valores vazios com o último valor válido --------------------- \n")

# ffill preenche com o último valor válido
dados_DF['Total Vendas'] = dados_DF['Total Vendas'].ffill()

print(dados_DF)

#             Vendedor Data Venda  Total Vendas
# 0     Amanda Martins 2023-01-01         751.0
# 1     Amanda Martins 2023-01-02         988.0
# 2     Eliane Moreira 2023-01-03         688.0
# 3     Eliane Moreira 2023-01-04         255.0
# 4    Gabriel Cardoso 2023-01-05         281.0
# 5    Gabriel Cardoso 2023-01-06         381.0
# 6    Ismael Silveira 2023-01-07         273.0
# 7    Ismael Silveira 2023-01-08         932.0
# 8    Ismael Silveira 2023-01-09         381.0
# 9   Leonardo Almeida 2023-01-10         479.0
# 10  Leonardo Almeida 2023-01-11         469.0
# 11   Nicolas Pereira 2023-01-12         502.0
# 12   Nicolas Pereira 2023-01-13         502.0
# 13      Paulo Santos 2023-01-14         502.0
# 14      Paulo Santos 2023-01-15         502.0
# 15   Rodolfo Martins 2023-01-02         502.0
# 16   Rodolfo Martins 2023-01-03         502.0
# 17   Rodolfo Martins 2023-01-04         502.0
# 18     Rodrigo Pires 2023-01-05         502.0
# 19     Rodrigo Pires 2023-01-06         502.0
# 20     Rodrigo Pires 2023-01-07         502.0

print("\n --------------------- Imprime quantas linhas / vendas foram feitas --------------------- \n")

# value_counts = conta em quantas linhas cada vendedor aparece / vendas foram feitas
qtdVendas = dados_DF["Vendedor"].value_counts()

print(qtdVendas)

# Ismael Silveira     3
# Rodolfo Martins     3
# Rodrigo Pires       3
# Amanda Martins      2
# Eliane Moreira      2
# Gabriel Cardoso     2
# Leonardo Almeida    2
# Nicolas Pereira     2
# Paulo Santos        2
# Name: Vendedor, dtype: int64

print("\n --------------------- Agrupando informações --------------------- \n")

# groupby agrupa informações
# sum() -> soma
vendaVendedor = dados_DF.groupby("Vendedor").sum()

print(vendaVendedor)

#                   Total Vendas
# Vendedor
# Amanda Martins          1739.0
# Eliane Moreira           943.0
# Gabriel Cardoso          662.0
# Ismael Silveira         1586.0
# Leonardo Almeida         948.0
# Nicolas Pereira         1004.0
# Paulo Santos            1004.0
# Rodolfo Martins         1506.0
# Rodrigo Pires           1506.0
