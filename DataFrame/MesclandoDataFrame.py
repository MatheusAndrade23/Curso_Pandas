# Abrindo arquivo deo Excel
import pandas as pd

vendasJaneiro_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendas_Jan.xlsx', engine="openpyxl")

vendasFevereiro_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendas_Fev.xlsx', engine="openpyxl")

vendasMarco_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendas_Mar.xlsx', engine="openpyxl")


print("\n --------------------- Unindo os arquivos de vendas Janeiro e Fevereiro --------------------- \n")

# concat junta as informações
vendasJaneiro_Fevereiro_DF = pd.concat([vendasJaneiro_DF, vendasFevereiro_DF])

print(vendasJaneiro_Fevereiro_DF)

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
# 0   Leonardo Almeida                 Tênis Feminino 2023-02-01        719.92
# 1     Eliane Moreira          Calça Feminina Jogger 2023-02-02        139.98
# 2    Nicolas Pereira               Camisa Masculina 2023-02-03        306.80
# 3     Amanda Martins              Bermuda Masculino 2023-02-04       1485.60
# 4       Paulo Santos  Camisa Masculina Festa Balada 2023-02-05        876.84
# 5    Gabriel Cardoso                 Bota Masculina 2023-02-06        448.28
# 6   Leonardo Almeida        Jaqueta Masculina Preta 2023-02-07        602.00
# 7     Eliane Moreira              Bolsa de Trabalho 2023-02-08        994.92
# 8    Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-02-09       1048.68
# 9     Amanda Martins               Vestido Infantil 2023-02-10         59.90
# 10  Leonardo Almeida                Calça Bailarina 2023-02-11        281.40
# 11    Eliane Moreira                 Camisa Térmica 2023-02-12         83.80
# 12   Nicolas Pereira                  Sapato Social 2023-02-13        573.30
# 13    Amanda Martins               Sapatilha Sapato 2023-02-14        503.10
# 14    Eliane Moreira                 Colar Pingente 2023-02-15        719.20
# 15      Angela Maria                 Tênis Feminino 2023-02-16        359.96
# 16    Carlos Moreira          Calça Feminina Jogger 2023-02-17        489.93
# 17    Eliane Moreira               Camisa Masculina 2023-02-18       1073.80
# 18   Nicolas Pereira              Bermuda Masculino 2023-02-19       1039.92
# 19  Leonardo Almeida  Camisa Masculina Festa Balada 2023-02-20       1315.26
# 20   Gabriel Cardoso                 Bota Masculina 2023-02-21       1344.84
# 21  Leonardo Almeida        Jaqueta Masculina Preta 2023-02-22        903.00
# 22    Eliane Moreira              Bolsa de Trabalho 2023-02-23        994.92
# 23   Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-02-24       1048.68
# 24    Amanda Martins               Vestido Infantil 2023-02-25        479.20
# 25    Eliane Moreira                Calça Bailarina 2023-02-26        234.50
# 26   Nicolas Pereira                 Camisa Térmica 2023-02-27        377.10
# 27    Amanda Martins                  Sapato Social 2023-02-28        737.10

print("\n --------------------- Unindo os arquivos de vendas Janeiro e Fevereiro e Março --------------------- \n")

# concat junta as informações
vendasGeral_DF = pd.concat(
    [vendasJaneiro_DF, vendasFevereiro_DF, vendasMarco_DF])

print(vendasGeral_DF)

#             Vendedor                        Produto Data Venda  Total Vendas
# 0   Leonardo Almeida                 Tênis Feminino 2023-01-01        719.92
# 1     Eliane Moreira          Calça Feminina Jogger 2023-01-02        139.98
# 2    Nicolas Pereira               Camisa Masculina 2023-01-03        306.80
# 3     Amanda Martins              Bermuda Masculino 2023-01-04       1485.60
# 4       Paulo Santos  Camisa Masculina Festa Balada 2023-01-05        876.84
# ..               ...                            ...        ...           ...
# 23   Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-03-24       1048.68
# 24    Amanda Martins               Vestido Infantil 2023-03-25       1437.60
# 25    Eliane Moreira                Calça Bailarina 2023-03-26        844.20
# 26   Nicolas Pereira                 Camisa Térmica 2023-03-27       1257.00
# 27    Amanda Martins                  Sapato Social 2023-03-28       1392.30


print("\n --------------------- Resumindo DataFrame Geral --------------------- \n")

resumoDataFrameGeral = vendasGeral_DF[[
    "Vendedor", "Data Venda", "Total Vendas"]]

print(resumoDataFrameGeral)

#             Vendedor Data Venda  Total Vendas
# 0   Leonardo Almeida 2023-01-01        719.92
# 1     Eliane Moreira 2023-01-02        139.98
# 2    Nicolas Pereira 2023-01-03        306.80
# 3     Amanda Martins 2023-01-04       1485.60
# 4       Paulo Santos 2023-01-05        876.84
# ..               ...        ...           ...
# 23   Nicolas Pereira 2023-03-24       1048.68
# 24    Amanda Martins 2023-03-25       1437.60
# 25    Eliane Moreira 2023-03-26        844.20
# 26   Nicolas Pereira 2023-03-27       1257.00
# 27    Amanda Martins 2023-03-28       1392.30

print("\n --------------------- Vendas com Grupos --------------------- \n")

vendasGeralGrupos_DF = pd.concat(
    [vendasJaneiro_DF, vendasFevereiro_DF, vendasMarco_DF], keys=['Janeiro', 'Fevereiro', 'Março'])

print(vendasGeralGrupos_DF)

#                     Vendedor                        Produto Data Venda  Total Vendas
# Janeiro 0   Leonardo Almeida                 Tênis Feminino 2023-01-01        719.92
#         1     Eliane Moreira          Calça Feminina Jogger 2023-01-02        139.98
#         2    Nicolas Pereira               Camisa Masculina 2023-01-03        306.80
#         3     Amanda Martins              Bermuda Masculino 2023-01-04       1485.60
#         4       Paulo Santos  Camisa Masculina Festa Balada 2023-01-05        876.84
# ...                      ...                            ...        ...           ...
# Março   23   Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-03-24       1048.68
#         24    Amanda Martins               Vestido Infantil 2023-03-25       1437.60
#         25    Eliane Moreira                Calça Bailarina 2023-03-26        844.20
#         26   Nicolas Pereira                 Camisa Térmica 2023-03-27       1257.00
#         27    Amanda Martins                  Sapato Social 2023-03-28       1392.30

print("\n --------------------- Extraindo o Mes de Fevereiro --------------------- \n")

extraindoFevereiro = vendasGeralGrupos_DF.loc['Fevereiro']
print(extraindoFevereiro)

# Vendedor                        Produto Data Venda  Total Vendas
# 0   Leonardo Almeida                 Tênis Feminino 2023-02-01        719.92
# 1     Eliane Moreira          Calça Feminina Jogger 2023-02-02        139.98
# 2    Nicolas Pereira               Camisa Masculina 2023-02-03        306.80
# 3     Amanda Martins              Bermuda Masculino 2023-02-04       1485.60
# 4       Paulo Santos  Camisa Masculina Festa Balada 2023-02-05        876.84
# 5    Gabriel Cardoso                 Bota Masculina 2023-02-06        448.28
# 6   Leonardo Almeida        Jaqueta Masculina Preta 2023-02-07        602.00
# 7     Eliane Moreira              Bolsa de Trabalho 2023-02-08        994.92
# 8    Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-02-09       1048.68
# 9     Amanda Martins               Vestido Infantil 2023-02-10         59.90
# 10  Leonardo Almeida                Calça Bailarina 2023-02-11        281.40
# 11    Eliane Moreira                 Camisa Térmica 2023-02-12         83.80
# 12   Nicolas Pereira                  Sapato Social 2023-02-13        573.30
# 13    Amanda Martins               Sapatilha Sapato 2023-02-14        503.10
# 14    Eliane Moreira                 Colar Pingente 2023-02-15        719.20
# 15      Angela Maria                 Tênis Feminino 2023-02-16        359.96
# 16    Carlos Moreira          Calça Feminina Jogger 2023-02-17        489.93
# 17    Eliane Moreira               Camisa Masculina 2023-02-18       1073.80
# 18   Nicolas Pereira              Bermuda Masculino 2023-02-19       1039.92
# 19  Leonardo Almeida  Camisa Masculina Festa Balada 2023-02-20       1315.26
# 20   Gabriel Cardoso                 Bota Masculina 2023-02-21       1344.84
# 21  Leonardo Almeida        Jaqueta Masculina Preta 2023-02-22        903.00
# 22    Eliane Moreira              Bolsa de Trabalho 2023-02-23        994.92
# 23   Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-02-24       1048.68
# 24    Amanda Martins               Vestido Infantil 2023-02-25        479.20
# 25    Eliane Moreira                Calça Bailarina 2023-02-26        234.50
# 26   Nicolas Pereira                 Camisa Térmica 2023-02-27        377.10
# 27    Amanda Martins                  Sapato Social 2023-02-28        737.10
