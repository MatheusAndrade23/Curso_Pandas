import pandas as pd

# Abrindo arquivo deo Excel
vendas_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendas_Jan.xlsx', engine="openpyxl")

print(vendas_DF)

#             Vendedor                        Produto Data Venda  Total Vendas
# 0   Leonardo Almeida                 Tênis Feminino 2023-01-01        719.92
# 1     Eliane Moreira          Calça Feminina Jogger 2023-01-02        139.98
# 2    Nicolas Pereira               Camisa Masculina 2023-01-03        306.80
# 3     Amanda Martins              Bermuda Masculino 2023-01-04       1485.60
# 4       Paulo Santos  Camisa Masculina Festa Balada 2023-01-05        876.84
# 5    Gabriel Cardoso                 Bota Masculina 2023-01-06        448.28
# 6   Leonardo Almeida        Jaqueta Masculina Preta 2023-01-07        602.00
# 7     Eliane Moreira              Bolsa de Trabalho 2023-01-08        994.92
# 8    Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-01-09       1048.68
# 9     Amanda Martins               Vestido Infantil 2023-01-10         59.90
# 10  Leonardo Almeida                Calça Bailarina 2023-01-11        281.40
# 11    Eliane Moreira                 Camisa Térmica 2023-01-12         83.80
# 12   Nicolas Pereira                  Sapato Social 2023-01-13        573.30
# 13    Amanda Martins               Sapatilha Sapato 2023-01-14        503.10
# 14    Eliane Moreira                 Colar Pingente 2023-01-15        719.20
# 15      Angela Maria                 Tênis Feminino 2023-01-16        359.96
# 16    Carlos Moreira          Calça Feminina Jogger 2023-01-17        489.93
# 17    Eliane Moreira               Camisa Masculina 2023-01-18       1073.80
# 18   Nicolas Pereira              Bermuda Masculino 2023-01-19       1039.92
# 19  Leonardo Almeida  Camisa Masculina Festa Balada 2023-01-20       1315.26
# 20   Gabriel Cardoso                 Bota Masculina 2023-01-21       1344.84
# 21  Leonardo Almeida        Jaqueta Masculina Preta 2023-01-22        903.00
# 22    Eliane Moreira              Bolsa de Trabalho 2023-01-23        994.92
# 23   Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-01-24       1048.68
# 24    Amanda Martins               Vestido Infantil 2023-01-25        479.20
# 25    Eliane Moreira                Calça Bailarina 2023-01-26        234.50
# 26   Nicolas Pereira                 Camisa Térmica 2023-01-27        377.10
# 27    Amanda Martins                  Sapato Social 2023-01-28        737.10

print("\n --------------------- Index exibe apenas informações sobre as linhas do DataFrame --------------------- \n")

print(vendas_DF.index)

# RangeIndex(start=0, stop=28, step=1)

print("\n --------------------- Exibe o nome de todas as colunas do DataFrame --------------------- \n")

print(vendas_DF.columns)

# Index(['Vendedor', 'Produto', 'Data Venda', 'Total Vendas'], dtype='object')

print("\n --------------------- Exibe apenas as 5 primeiras linhas por padrão --------------------- \n")

print(vendas_DF.head())

#            Vendedor                        Produto Data Venda  Total Vendas
# 0  Leonardo Almeida                 Tênis Feminino 2023-01-01        719.92
# 1    Eliane Moreira          Calça Feminina Jogger 2023-01-02        139.98
# 2   Nicolas Pereira               Camisa Masculina 2023-01-03        306.80
# 3    Amanda Martins              Bermuda Masculino 2023-01-04       1485.60
# 4      Paulo Santos  Camisa Masculina Festa Balada 2023-01-05        876.84

print("\n --------------------- Exibe apenas as 10 primeiras linhas --------------------- \n")

print(vendas_DF.head(10))

#            Vendedor                        Produto Data Venda  Total Vendas
# 0  Leonardo Almeida                 Tênis Feminino 2023-01-01        719.92
# 1    Eliane Moreira          Calça Feminina Jogger 2023-01-02        139.98
# 2   Nicolas Pereira               Camisa Masculina 2023-01-03        306.80
# 3    Amanda Martins              Bermuda Masculino 2023-01-04       1485.60
# 4      Paulo Santos  Camisa Masculina Festa Balada 2023-01-05        876.84
# 5   Gabriel Cardoso                 Bota Masculina 2023-01-06        448.28
# 6  Leonardo Almeida        Jaqueta Masculina Preta 2023-01-07        602.00
# 7    Eliane Moreira              Bolsa de Trabalho 2023-01-08        994.92
# 8   Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-01-09       1048.68
# 9    Amanda Martins               Vestido Infantil 2023-01-10         59.90

print("\n --------------------- Exibe apenas as  3 ultimas linhas --------------------- \n")

print(vendas_DF.tail(3))

#            Vendedor          Produto Data Venda  Total Vendas
# 25   Eliane Moreira  Calça Bailarina 2023-01-26         234.5
# 26  Nicolas Pereira   Camisa Térmica 2023-01-27         377.1
# 27   Amanda Martins    Sapato Social 2023-01-28         737.1

print("\n --------------------- Imprimindo somente a coluna 'Vendedor' --------------------- \n")

print(vendas_DF["Vendedor"])

# 0     Leonardo Almeida
# 1       Eliane Moreira
# 2      Nicolas Pereira
# 3       Amanda Martins
# 4         Paulo Santos
# 5      Gabriel Cardoso
# 6     Leonardo Almeida
# 7       Eliane Moreira
# 8      Nicolas Pereira
# 9       Amanda Martins
# 10    Leonardo Almeida
# 11      Eliane Moreira
# 12     Nicolas Pereira
# 13      Amanda Martins
# 14      Eliane Moreira
# 15        Angela Maria
# 16      Carlos Moreira
# 17      Eliane Moreira
# 18     Nicolas Pereira
# 19    Leonardo Almeida
# 20     Gabriel Cardoso
# 21    Leonardo Almeida
# 22      Eliane Moreira
# 23     Nicolas Pereira
# 24      Amanda Martins
# 25      Eliane Moreira
# 26     Nicolas Pereira
# 27      Amanda Martins


print("\n --------------------- Imprimindo somente a coluna 'Vendedor' e 'Total Vendas' --------------------- \n")

print(vendas_DF[["Vendedor", "Total Vendas"]])

#             Vendedor  Total Vendas
# 0   Leonardo Almeida        719.92
# 1     Eliane Moreira        139.98
# 2    Nicolas Pereira        306.80
# 3     Amanda Martins       1485.60
# 4       Paulo Santos        876.84
# 5    Gabriel Cardoso        448.28
# 6   Leonardo Almeida        602.00
# 7     Eliane Moreira        994.92
# 8    Nicolas Pereira       1048.68
# 9     Amanda Martins         59.90
# 10  Leonardo Almeida        281.40
# 11    Eliane Moreira         83.80
# 12   Nicolas Pereira        573.30
# 13    Amanda Martins        503.10
# 14    Eliane Moreira        719.20
# 15      Angela Maria        359.96
# 16    Carlos Moreira        489.93
# 17    Eliane Moreira       1073.80
# 22    Eliane Moreira        994.92
# 23   Nicolas Pereira       1048.68
# 24    Amanda Martins        479.20
# 25    Eliane Moreira        234.50
# 26   Nicolas Pereira        377.10
# 27    Amanda Martins        737.10

print("\n --------------------- Imprimindo somente linhas de 0 a 2 --------------------- \n")

print(vendas_DF.loc[0:2])

#            Vendedor                Produto Data Venda  Total Vendas
# 0  Leonardo Almeida         Tênis Feminino 2023-01-01        719.92
# 1    Eliane Moreira  Calça Feminina Jogger 2023-01-02        139.98
# 2   Nicolas Pereira       Camisa Masculina 2023-01-03        306.80


print("\n --------------------- Imprimindo somente as linhas onde o Leonardo é o vendedor --------------------- \n")

vendas_LeonardoAlmeida_DF = vendas_DF.loc[vendas_DF["Vendedor"]
                                          == "Leonardo Almeida"]

print(vendas_LeonardoAlmeida_DF)

#             Vendedor                        Produto Data Venda  Total Vendas
# 0   Leonardo Almeida                 Tênis Feminino 2023-01-01        719.92
# 6   Leonardo Almeida        Jaqueta Masculina Preta 2023-01-07        602.00
# 10  Leonardo Almeida                Calça Bailarina 2023-01-11        281.40
# 19  Leonardo Almeida  Camisa Masculina Festa Balada 2023-01-20       1315.26
# 21  Leonardo Almeida        Jaqueta Masculina Preta 2023-01-22        903.00

print("\n --------------------- Imprimindo somente o total de vendas do Leonardo almeida --------------------- \n")

vendas_LeonardoAlmeida_Resumida_DF = vendas_DF.loc[vendas_DF["Vendedor"]
                                                   == "Leonardo Almeida", ["Vendedor", "Total Vendas"]]

print(vendas_LeonardoAlmeida_Resumida_DF)

#             Vendedor  Total Vendas
# 0   Leonardo Almeida        719.92
# 6   Leonardo Almeida        602.00
# 10  Leonardo Almeida        281.40
# 19  Leonardo Almeida       1315.26
# 21  Leonardo Almeida        903.00

print("\n --------------------- Vendedor da linha 4 --------------------- \n")

print(vendas_DF.loc[4, "Vendedor"])

# Paulo Santos

print("\n --------------------- Imprime quantas linhas e colunas tem nosso DF --------------------- \n")

print(vendas_DF.shape)

# (28, 4)

print("\n --------------------- Transforma linhas em colunas e colunas em linhas --------------------- \n")

# T = Transforma linhas emcolunas e colunas em linhas
transformarLinhasEmColunas = vendas_DF.T

print(transformarLinhasEmColunas)

#                                0                      1   ...                   26                   27
# Vendedor         Leonardo Almeida         Eliane Moreira  ...      Nicolas Pereira       Amanda Martins
# Produto            Tênis Feminino  Calça Feminina Jogger  ...       Camisa Térmica        Sapato Social
# Data Venda    2023-01-01 00:00:00    2023-01-02 00:00:00  ...  2023-01-27 00:00:00  2023-01-28 00:00:00
# Total Vendas               719.92                 139.98  ...                377.1                737.1

# [4 rows x 28 columns]

print("\n --------------------- Deletar linhas que tenham pelo menos 1 valor em branco --------------------- \n")

# dropna deleta as linhas que tenham pelo menos 1 valor em branco
deletandoLinhasEmBranco = vendas_DF.dropna()

print(deletandoLinhasEmBranco)

print("\n --------------------- Deletar coluna 'Vendedor' --------------------- \n")

# del deleta a coluna

# del vendas_DF["Vendedor"]

# print(vendas_DF)

#                            Produto Data Venda  Total Vendas
# 0                  Tênis Feminino 2023-01-01        719.92
# 1           Calça Feminina Jogger 2023-01-02        139.98
# 16          Calça Feminina Jogger 2023-01-17        489.93
# 17               Camisa Masculina 2023-01-18       1073.80
# 18              Bermuda Masculino 2023-01-19       1039.92
# 19  Camisa Masculina Festa Balada 2023-01-20       1315.26
# 20                 Bota Masculina 2023-01-21       1344.84
# 21        Jaqueta Masculina Preta 2023-01-22        903.00
# 22              Bolsa de Trabalho 2023-01-23        994.92
# 23    Kit de Pinceis de Maquiagem 2023-01-24       1048.68
# 24               Vestido Infantil 2023-01-25        479.20
# 25                Calça Bailarina 2023-01-26        234.50
# 26                 Camisa Térmica 2023-01-27        377.10
# 27                  Sapato Social 2023-01-28        737.10

print("\n --------------------- Deletando mais de uma coluna --------------------- \n")

deletarDuasColunas = vendas_DF.drop(columns=["Vendedor", "Total Vendas"])

print(deletarDuasColunas)

#                           Produto Data Venda
# 0                  Tênis Feminino 2023-01-01
# 1           Calça Feminina Jogger 2023-01-02
# 2                Camisa Masculina 2023-01-03
# 3               Bermuda Masculino 2023-01-04
# 4   Camisa Masculina Festa Balada 2023-01-05
# 5                  Bota Masculina 2023-01-06
# 6         Jaqueta Masculina Preta 2023-01-07
# 7               Bolsa de Trabalho 2023-01-08
# 8     Kit de Pinceis de Maquiagem 2023-01-09
# 9                Vestido Infantil 2023-01-10
# 10                Calça Bailarina 2023-01-11
# 11                 Camisa Térmica 2023-01-12
# 12                  Sapato Social 2023-01-13
# 13               Sapatilha Sapato 2023-01-14
# 14                 Colar Pingente 2023-01-15
# 15                 Tênis Feminino 2023-01-16
# 16          Calça Feminina Jogger 2023-01-17
# 17               Camisa Masculina 2023-01-18
# 18              Bermuda Masculino 2023-01-19
# 19  Camisa Masculina Festa Balada 2023-01-20
# 20                 Bota Masculina 2023-01-21
# 21        Jaqueta Masculina Preta 2023-01-22
# 22              Bolsa de Trabalho 2023-01-23
# 23    Kit de Pinceis de Maquiagem 2023-01-24
# 24               Vestido Infantil 2023-01-25
# 25                Calça Bailarina 2023-01-26
# 26                 Camisa Térmica 2023-01-27
# 27                  Sapato Social 2023-01-28

print("\n --------------------- Excluir Linha 3 --------------------- \n")

# axis = eixo -> 1 - Coluna, 0 - Linha
excluirLinha3 = deletarDuasColunas.drop(2, axis=0)

print(excluirLinha3)

# 0                  Tênis Feminino 2023-01-01
# 1           Calça Feminina Jogger 2023-01-02
# 3               Bermuda Masculino 2023-01-04
# 4   Camisa Masculina Festa Balada 2023-01-05
# 5                  Bota Masculina 2023-01-06
# 6         Jaqueta Masculina Preta 2023-01-07
# 7               Bolsa de Trabalho 2023-01-08
# 8     Kit de Pinceis de Maquiagem 2023-01-09
# 9                Vestido Infantil 2023-01-10
# 10                Calça Bailarina 2023-01-11
# 11                 Camisa Térmica 2023-01-12
# 12                  Sapato Social 2023-01-13
# 13               Sapatilha Sapato 2023-01-14
# 14                 Colar Pingente 2023-01-15
# 15                 Tênis Feminino 2023-01-16
# 16          Calça Feminina Jogger 2023-01-17
# 17               Camisa Masculina 2023-01-18
# 18              Bermuda Masculino 2023-01-19
# 19  Camisa Masculina Festa Balada 2023-01-20
# 20                 Bota Masculina 2023-01-21
# 21        Jaqueta Masculina Preta 2023-01-22
# 22              Bolsa de Trabalho 2023-01-23
# 23    Kit de Pinceis de Maquiagem 2023-01-24
# 24               Vestido Infantil 2023-01-25
# 25                Calça Bailarina 2023-01-26
# 26                 Camisa Térmica 2023-01-27
# 27                  Sapato Social 2023-01-28


print("\n --------------------- Excluir mais linhas --------------------- \n")

# axis = eixo -> 1 - Coluna, 0 - Linha
excluirMaisLinhas = deletarDuasColunas.drop([0, 1])

print(excluirMaisLinhas)

#                          Produto Data Venda
# 2                Camisa Masculina 2023-01-03
# 3               Bermuda Masculino 2023-01-04
# 4   Camisa Masculina Festa Balada 2023-01-05
# 5                  Bota Masculina 2023-01-06
# 6         Jaqueta Masculina Preta 2023-01-07
# 7               Bolsa de Trabalho 2023-01-08
# 8     Kit de Pinceis de Maquiagem 2023-01-09
# 9                Vestido Infantil 2023-01-10
# 10                Calça Bailarina 2023-01-11
# 11                 Camisa Térmica 2023-01-12
# 12                  Sapato Social 2023-01-13
# 13               Sapatilha Sapato 2023-01-14
# 14                 Colar Pingente 2023-01-15
# 15                 Tênis Feminino 2023-01-16
# 16          Calça Feminina Jogger 2023-01-17
# 17               Camisa Masculina 2023-01-18
# 18              Bermuda Masculino 2023-01-19
# 19  Camisa Masculina Festa Balada 2023-01-20
# 20                 Bota Masculina 2023-01-21
# 21        Jaqueta Masculina Preta 2023-01-22
# 22              Bolsa de Trabalho 2023-01-23
# 23    Kit de Pinceis de Maquiagem 2023-01-24
# 24               Vestido Infantil 2023-01-25
# 25                Calça Bailarina 2023-01-26
# 26                 Camisa Térmica 2023-01-27
# 27                  Sapato Social 2023-01-28
