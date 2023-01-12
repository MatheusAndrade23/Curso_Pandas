import pandas as pd

# Abrindo arquivo do Excel
produtos_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Produtos_Merge.xlsx', engine="openpyxl")

# Abrindo arquivo do Excel
vendas_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendas_Merge.xlsx', engine="openpyxl")

# Abrindo arquivo do Excel
vendedores_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Vendedores_Merge.xlsx', engine="openpyxl")


print("\n --------------------- Merge Vendas e Vendedores --------------------- \n")

# merge une informações das tabelas com base em identificadores (uma coluna em comum)
vendas_DF = vendas_DF.merge(vendedores_DF)

print(vendas_DF)

#     Id Vendedor  ID Produto Data Venda  Quantidade Vendida  Valor Unitário  Total Vendas          Vendedor  Meta
# 0         27264      100482 2023-01-01                   8           89.99        719.92  Leonardo Almeida  5000
# 1         27264      100345 2023-01-07                   4          150.50        602.00  Leonardo Almeida  5000
# 2         27264      100208 2023-01-11                   6           46.90        281.40  Leonardo Almeida  5000
# 3         27264      100244 2023-01-20                   9          146.14       1315.26  Leonardo Almeida  5000
# 4         27264      100345 2023-01-22                   6          150.50        903.00  Leonardo Almeida  5000
# 5         21732      100359 2023-01-02                   2           69.99        139.98    Eliane Moreira  5000
# 6         21732      100411 2023-01-08                   4          248.73        994.92    Eliane Moreira  5000
# 7         21732      100226 2023-01-12                   2           41.90         83.80    Eliane Moreira  5000
# 8         21732      100001 2023-01-15                   8           89.90        719.20    Eliane Moreira  5000
# 9         21732      100105 2023-01-18                   7          153.40       1073.80    Eliane Moreira  5000
# 10        21732      100411 2023-01-23                   4          248.73        994.92    Eliane Moreira  5000
# 11        21732      100208 2023-01-26                   5           46.90        234.50    Eliane Moreira  5000
# 12        27082      100105 2023-01-03                   2          153.40        306.80   Nicolas Pereira  5000
# 13        27082      100128 2023-01-09                   9          116.52       1048.68   Nicolas Pereira  5000
# 14        27082      100128 2023-01-13                   7           81.90        573.30   Nicolas Pereira  5000
# 15        27082      100212 2023-01-19                   7          148.56       1039.92   Nicolas Pereira  5000
# 16        27082      100128 2023-01-24                   9          116.52       1048.68   Nicolas Pereira  5000
# 17        27082      100226 2023-01-27                   9           41.90        377.10   Nicolas Pereira  5000
# 18        22936      100212 2023-01-04                  10          148.56       1485.60    Amanda Martins  5000
# 19        22936      100877 2023-01-10                   1           59.90         59.90    Amanda Martins  5000
# 20        22936      100443 2023-01-14                   9           55.90        503.10    Amanda Martins  5000
# 21        22936      100877 2023-01-25                   8           59.90        479.20    Amanda Martins  5000
# 22        22936      100128 2023-01-28                   9           81.90        737.10    Amanda Martins  5000
# 23        21164      100244 2023-01-05                   6          146.14        876.84      Paulo Santos  5000
# 24        28824      100301 2023-01-06                   2          224.14        448.28   Gabriel Cardoso  5000
# 25        28824      100301 2023-01-21                   6          224.14       1344.84   Gabriel Cardoso  5000
# 26        37579      100482 2023-01-16                   4           89.99        359.96      Angela Maria  5000
# 27        20437      100359 2023-01-17                   7           69.99        489.93    Carlos Moreira  5000

print("\n --------------------- Merge Vendas e Produtos --------------------- \n")

# merge une informações das tabelas com base em identificadores (uma coluna em comum)
vendas_DF = vendas_DF.merge(produtos_DF)

print(vendas_DF)

#     Id Vendedor  ID Produto Data Venda  Quantidade Vendida  Valor Unitário  Total Vendas          Vendedor  Meta                        Produto
# 0         27264      100482 2023-01-01                   8           89.99        719.92  Leonardo Almeida  5000                 Tênis Feminino
# 1         37579      100482 2023-01-16                   4           89.99        359.96      Angela Maria  5000                 Tênis Feminino
# 2         27264      100345 2023-01-07                   4          150.50        602.00  Leonardo Almeida  5000        Jaqueta Masculina Preta
# 3         27264      100345 2023-01-22                   6          150.50        903.00  Leonardo Almeida  5000        Jaqueta Masculina Preta
# 4         27264      100208 2023-01-11                   6           46.90        281.40  Leonardo Almeida  5000                Calça Bailarina
# 5         21732      100208 2023-01-26                   5           46.90        234.50    Eliane Moreira  5000                Calça Bailarina
# 6         27264      100244 2023-01-20                   9          146.14       1315.26  Leonardo Almeida  5000  Camisa Masculina Festa Balada
# 7         21164      100244 2023-01-05                   6          146.14        876.84      Paulo Santos  5000  Camisa Masculina Festa Balada
# 8         21732      100359 2023-01-02                   2           69.99        139.98    Eliane Moreira  5000          Calça Feminina Jogger
# 9         20437      100359 2023-01-17                   7           69.99        489.93    Carlos Moreira  5000          Calça Feminina Jogger
# 10        21732      100411 2023-01-08                   4          248.73        994.92    Eliane Moreira  5000              Bolsa de Trabalho
# 11        21732      100411 2023-01-23                   4          248.73        994.92    Eliane Moreira  5000              Bolsa de Trabalho
# 12        21732      100226 2023-01-12                   2           41.90         83.80    Eliane Moreira  5000                 Camisa Térmica
# 13        27082      100226 2023-01-27                   9           41.90        377.10   Nicolas Pereira  5000                 Camisa Térmica
# 14        21732      100001 2023-01-15                   8           89.90        719.20    Eliane Moreira  5000                 Colar Pingente
# 15        21732      100105 2023-01-18                   7          153.40       1073.80    Eliane Moreira  5000               Camisa Masculina
# 16        27082      100105 2023-01-03                   2          153.40        306.80   Nicolas Pereira  5000               Camisa Masculina
# 17        27082      100128 2023-01-09                   9          116.52       1048.68   Nicolas Pereira  5000    Kit de Pinceis de Maquiagem
# 18        27082      100128 2023-01-24                   9          116.52       1048.68   Nicolas Pereira  5000    Kit de Pinceis de Maquiagem
# 19        27082      100128 2023-01-13                   7           81.90        573.30   Nicolas Pereira  5000                  Sapato Social
# 20        22936      100128 2023-01-28                   9           81.90        737.10    Amanda Martins  5000                  Sapato Social
# 21        27082      100212 2023-01-19                   7          148.56       1039.92   Nicolas Pereira  5000              Bermuda Masculino
# 22        22936      100212 2023-01-04                  10          148.56       1485.60    Amanda Martins  5000              Bermuda Masculino
# 23        22936      100877 2023-01-10                   1           59.90         59.90    Amanda Martins  5000               Vestido Infantil
# 24        22936      100877 2023-01-25                   8           59.90        479.20    Amanda Martins  5000               Vestido Infantil
# 25        22936      100443 2023-01-14                   9           55.90        503.10    Amanda Martins  5000               Sapatilha Sapato
# 26        28824      100301 2023-01-06                   2          224.14        448.28   Gabriel Cardoso  5000                 Bota Masculina
# 27        28824      100301 2023-01-21                   6          224.14       1344.84   Gabriel Cardoso  5000                 Bota Masculina

print(vendas_DF.columns)

# Index(['Id Vendedor', 'ID Produto', 'Data Venda', 'Quantidade Vendida',
#        'Valor Unitário', 'Total Vendas', 'Vendedor', 'Meta', 'Produto'],
#       dtype='object')

print("\n --------------------- Resumo do DataFrame --------------------- \n")

resumoDF = vendas_DF[["Vendedor", "Produto", "Total Vendas"]]

print(resumoDF)

#             Vendedor                        Produto  Total Vendas
# 0   Leonardo Almeida                 Tênis Feminino        719.92
# 1       Angela Maria                 Tênis Feminino        359.96
# 2   Leonardo Almeida        Jaqueta Masculina Preta        602.00
# 3   Leonardo Almeida        Jaqueta Masculina Preta        903.00
# 4   Leonardo Almeida                Calça Bailarina        281.40
# 5     Eliane Moreira                Calça Bailarina        234.50
# 6   Leonardo Almeida  Camisa Masculina Festa Balada       1315.26
# 7       Paulo Santos  Camisa Masculina Festa Balada        876.84
# 8     Eliane Moreira          Calça Feminina Jogger        139.98
# 9     Carlos Moreira          Calça Feminina Jogger        489.93
# 10    Eliane Moreira              Bolsa de Trabalho        994.92
# 11    Eliane Moreira              Bolsa de Trabalho        994.92
# 12    Eliane Moreira                 Camisa Térmica         83.80
# 13   Nicolas Pereira                 Camisa Térmica        377.10
# 14    Eliane Moreira                 Colar Pingente        719.20
# 15    Eliane Moreira               Camisa Masculina       1073.80
# 16   Nicolas Pereira               Camisa Masculina        306.80
# 17   Nicolas Pereira    Kit de Pinceis de Maquiagem       1048.68
# 18   Nicolas Pereira    Kit de Pinceis de Maquiagem       1048.68
# 19   Nicolas Pereira                  Sapato Social        573.30
# 20    Amanda Martins                  Sapato Social        737.10
# 21   Nicolas Pereira              Bermuda Masculino       1039.92
# 22    Amanda Martins              Bermuda Masculino       1485.60
# 23    Amanda Martins               Vestido Infantil         59.90
# 24    Amanda Martins               Vestido Infantil        479.20
# 25    Amanda Martins               Sapatilha Sapato        503.10
# 26   Gabriel Cardoso                 Bota Masculina        448.28
# 27   Gabriel Cardoso                 Bota Masculina       1344.84
