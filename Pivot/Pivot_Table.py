import pandas as pd

baseLanchonete_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendas_Lanchonete_Pivot_Table.xlsx', engine="openpyxl")


print(baseLanchonete_DF)

#    Data Venda          Cliente      Produto  Preço Total  Preço com Desconto
# 0  2023-01-04     Angela Maria         Café            4                   2
# 1  2023-01-03   Carlos Moreira   Salgadinho            9                   7
# 2  2023-01-04  Gabriel Cardoso         Coca            8                   6
# 3  2023-01-02     Angela Maria      Bolinho           12                  10
# 4  2023-01-04   Carlos Moreira       Pastel           10                   8
# 5  2023-01-03     Angela Maria  Enroladinho            8                   6
# 6  2023-01-05   Carlos Moreira         Bolo           30                  28
# 7  2023-01-05  Gabriel Cardoso         Café            4                   2
# 8  2023-01-01     Paulo Santos   Salgadinho            9                   7
# 9  2023-01-01     Angela Maria         Coca            8                   6
# 10 2023-01-03   Carlos Moreira      Bolinho           12                  10
# 11 2023-01-04  Gabriel Cardoso       Pastel           10                   8
# 12 2023-01-02     Paulo Santos         Café            4                   2
# 13 2023-01-01     Angela Maria   Salgadinho            9                   7
# 14 2023-01-02   Carlos Moreira         Café            4                   2
# 15 2023-01-04  Gabriel Cardoso   Salgadinho            9                   7
# 16 2023-01-06     Paulo Santos         Coca            8                   6
# 17 2023-01-06     Angela Maria      Bolinho           12                  10
# 18 2023-01-03   Carlos Moreira         Café            4                   2
# 19 2023-01-02  Gabriel Cardoso   Salgadinho            9                   7
# 20 2023-01-01     Paulo Santos         Coca            8                   6
# 21 2023-01-03     Angela Maria      Bolinho           12                  10
# 22 2023-01-05   Carlos Moreira       Pastel           10                   8
# 23 2023-01-04     Angela Maria         Café            4                   2
# 24 2023-01-02     Angela Maria   Salgadinho            9                   7
# 25 2023-01-05   Carlos Moreira         Coca            8                   6
# 26 2023-01-01  Gabriel Cardoso      Bolinho           12                  10
# 27 2023-01-03     Paulo Santos       Pastel           10                   8


print("\n --------------- Imprimindo Data / Cliente / Preço com Desconto / Média ------------------\n")

# #index = Linhas
# #columns = Colunas
# #values = Soma
# #aggfunc = Tipo de calculo (sum - soma)
pivotExemplo1 = baseLanchonete_DF.pivot_table(
    index="Data Venda", columns="Cliente", values="Preço com Desconto", aggfunc="sum")


print(pivotExemplo1)

# Cliente     Angela Maria  Carlos Moreira  Gabriel Cardoso  Paulo Santos
# Data Venda
# 2023-01-01          13.0             NaN             10.0          13.0
# 2023-01-02          17.0             2.0              7.0           2.0
# 2023-01-03          16.0            19.0              NaN           8.0
# 2023-01-04           4.0             8.0             21.0           NaN
# 2023-01-05           NaN            42.0              2.0           NaN
# 2023-01-06          10.0             NaN              NaN           6.0


print("\n --------------- Imprimindo Cliente / Data Venda / Preço com Desconto / Média  ------------------\n")

# #index = Linhas
# #columns = Colunas
# #values = Soma
# #aggfunc = Tipo de calculo (sum - soma)
pivotExemplo2 = baseLanchonete_DF.pivot_table(
    index="Cliente", columns="Data Venda", values="Preço com Desconto", aggfunc="sum")


print(pivotExemplo2)

# Data Venda       2023-01-01  2023-01-02  2023-01-03  2023-01-04  2023-01-05  2023-01-06
# Cliente
# Angela Maria           13.0        17.0        16.0         4.0         NaN        10.0
# Carlos Moreira          NaN         2.0        19.0         8.0        42.0         NaN
# Gabriel Cardoso        10.0         7.0         NaN        21.0         2.0         NaN
# Paulo Santos           13.0         2.0         8.0         NaN         NaN         6.0


print("\n --------------- Imprimindo com Cliente / Preço Total e Preço com Desconto ------------------\n")

# #index = Linhas
# #columns = Colunas
# #values = Soma
# #aggfunc = Tipo de calculo (sum - soma)
pivotExemplo3 = baseLanchonete_DF.pivot_table(index="Data Venda", columns="Cliente", values=[
                                              "Preço Total", "Preço com Desconto"], aggfunc="sum")


print(pivotExemplo3)

#             Preço Total                                             Preço com Desconto
# Cliente    Angela Maria Carlos Moreira Gabriel Cardoso Paulo Santos       Angela Maria Carlos Moreira Gabriel Cardoso Paulo Santos
# Data Venda
# 2023-01-01         17.0            NaN            12.0         17.0               13.0            NaN            10.0         13.0
# 2023-01-02         21.0            4.0             9.0          4.0               17.0            2.0             7.0          2.0
# 2023-01-03         20.0           25.0             NaN         10.0               16.0           19.0             NaN          8.0
# 2023-01-04          8.0           10.0            27.0          NaN                4.0            8.0            21.0          NaN
# 2023-01-05          NaN           48.0             4.0          NaN                NaN           42.0             2.0          NaN
# 2023-01-06         12.0            NaN             NaN          8.0               10.0            NaN             NaN          6.0


print("\n --------------- Imprimindo com Cliente, Produto e Preço com Desconto ------------------\n")

# #index = Linhas
# #columns = Colunas
# #values = Soma
# #aggfunc = Tipo de calculo (sum - soma)
pivotExemplo4 = baseLanchonete_DF.pivot_table(index="Data Venda", columns=[
                                              "Cliente", "Produto"], values=["Preço Total", "Preço com Desconto"], aggfunc="sum")

print(pivotExemplo4)

#            Preço Total                                                                                                    ... Preço com Desconto

# Cliente    Angela Maria                                  Carlos Moreira                                   Gabriel Cardoso  ...     Carlos Moreira                   Gabriel Cardoso                             Paulo Santos

# Produto         Bolinho Café Coca Enroladinho Salgadinho        Bolinho  Bolo Café Coca Pastel Salgadinho         Bolinho  ...               Coca Pastel Salgadinho         Bolinho Café Coca Pastel Salgadinho         Café Coca Pastel Salgadinho
# Data Venda                                                                                                                 ...

# 2023-01-01          NaN  NaN  8.0         NaN        9.0            NaN   NaN  NaN  NaN    NaN        NaN            12.0  ...                NaN    NaN        NaN            10.0  NaN  NaN    NaN        NaN          NaN  6.0    NaN        7.0
# 2023-01-02         12.0  NaN  NaN         NaN        9.0            NaN   NaN  4.0  NaN    NaN        NaN             NaN  ...                NaN    NaN        NaN             NaN  NaN  NaN    NaN        7.0          2.0  NaN    NaN        NaN
# 2023-01-03         12.0  NaN  NaN         8.0        NaN           12.0   NaN  4.0  NaN    NaN        9.0             NaN  ...                NaN    NaN        7.0             NaN  NaN  NaN    NaN        NaN          NaN  NaN    8.0        NaN
# 2023-01-04          NaN  8.0  NaN         NaN        NaN            NaN   NaN  NaN  NaN   10.0        NaN             NaN  ...                NaN    8.0        NaN             NaN  NaN  6.0    8.0        7.0          NaN  NaN    NaN        NaN
# 2023-01-05          NaN  NaN  NaN         NaN        NaN            NaN  30.0  NaN  8.0   10.0        NaN             NaN  ...                6.0    8.0        NaN             NaN  2.0  NaN    NaN        NaN          NaN  NaN    NaN        NaN
# 2023-01-06         12.0  NaN  NaN         NaN        NaN            NaN   NaN  NaN  NaN    NaN        NaN             NaN  ...                NaN    NaN        NaN             NaN  NaN  NaN    NaN        NaN          NaN  6.0    NaN        NaN


print("\n ---------------  Trata NaN por ZERO ------------------\n")

# #index = Linhas
# #columns = Colunas
# #values = Soma
# #aggfunc = Tipo de calculo (sum - soma)

# #fillna - Preenche os valores vazios com algum valor
pivotExemplo4["Preço com Desconto"] = pivotExemplo4["Preço com Desconto"].fillna(
    0)
pivotExemplo4["Preço Total"] = pivotExemplo4["Preço Total"].fillna(0)


print(pivotExemplo4)

#             Preço Total                                                                                                    ... Preço com Desconto

# Cliente    Angela Maria                                  Carlos Moreira                                   Gabriel Cardoso  ...     Carlos Moreira                   Gabriel Cardoso                             Paulo Santos

# Produto         Bolinho Café Coca Enroladinho Salgadinho        Bolinho  Bolo Café Coca Pastel Salgadinho         Bolinho  ...               Coca Pastel Salgadinho         Bolinho Café Coca Pastel Salgadinho         Café Coca Pastel Salgadinho
# Data Venda                                                                                                                 ...

# 2023-01-01          0.0  0.0  8.0         0.0        9.0            0.0   0.0  0.0  0.0    0.0        0.0            12.0  ...                0.0    0.0        0.0            10.0  0.0  0.0    0.0        0.0          0.0  6.0    0.0        7.0
# 2023-01-02         12.0  0.0  0.0         0.0        9.0            0.0   0.0  4.0  0.0    0.0        0.0             0.0  ...                0.0    0.0        0.0             0.0  0.0  0.0    0.0        7.0          2.0  0.0    0.0        0.0
# 2023-01-03         12.0  0.0  0.0         8.0        0.0           12.0   0.0  4.0  0.0    0.0        9.0             0.0  ...                0.0    0.0        7.0             0.0  0.0  0.0    0.0        0.0          0.0  0.0    8.0        0.0
# 2023-01-04          0.0  8.0  0.0         0.0        0.0            0.0   0.0  0.0  0.0   10.0        0.0             0.0  ...                0.0    8.0        0.0             0.0  0.0  6.0    8.0        7.0          0.0  0.0    0.0        0.0
# 2023-01-05          0.0  0.0  0.0         0.0        0.0            0.0  30.0  0.0  8.0   10.0        0.0             0.0  ...                6.0    8.0        0.0             0.0  2.0  0.0    0.0        0.0          0.0  0.0    0.0        0.0
# 2023-01-06         12.0  0.0  0.0         0.0        0.0            0.0   0.0  0.0  0.0    0.0        0.0             0.0  ...                0.0    0.0        0.0             0.0  0.0  0.0    0.0        0.0          0.0  6.0    0.0        0.0

# [6 rows x 40 columns]
