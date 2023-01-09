import pandas as pd

# Abrindo arquivo do Excel
vendas_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Ordenacao.xlsx', engine="openpyxl")

print(vendas_DF)

print("\n --------------------- Ordenando os vendedores --------------------- \n")

ordenarVendedor = vendas_DF.sort_values(by="Vendedor")

print(ordenarVendedor)

#             Vendedor                        Produto Data Venda  Total Vendas
# 7     Amanda Martins               Vestido Infantil 2023-01-10         59.90
# 8     Amanda Martins              Bermuda Masculino 2023-01-04       1485.60
# 15    Amanda Martins               Sapatilha Sapato 2023-01-14        503.10
# 2       Angela Maria                 Tênis Feminino 2023-01-16        359.96
# 16    Carlos Moreira          Calça Feminina Jogger 2023-01-17        489.93
# 1     Eliane Moreira                 Colar Pingente 2023-01-15        719.20
# 5     Eliane Moreira          Calça Feminina Jogger 2023-01-02        139.98
# 17    Eliane Moreira               Camisa Masculina 2023-01-18       1073.80
# 10    Eliane Moreira                 Camisa Térmica 2023-01-12         83.80
# 14    Eliane Moreira              Bolsa de Trabalho 2023-01-08        994.92
# 3    Gabriel Cardoso                 Bota Masculina 2023-01-06        448.28
# 9   Leonardo Almeida                Calça Bailarina 2023-01-11        281.40
# 4   Leonardo Almeida                 Tênis Feminino 2023-01-01        719.92
# 13  Leonardo Almeida        Jaqueta Masculina Preta 2023-01-07        602.00
# 18   Nicolas Pereira              Bermuda Masculino 2023-01-19       1039.92
# 11   Nicolas Pereira                  Sapato Social 2023-01-13        573.30
# 6    Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-01-09       1048.68
# 12   Nicolas Pereira               Camisa Masculina 2023-01-03        306.80
# 0       Paulo Santos  Camisa Masculina Festa Balada 2023-01-05        876.84

print("\n --------------------- Ordenando os produtos --------------------- \n")

ordenarProdutos = vendas_DF.sort_values(by="Produto")

print(ordenarProdutos)

#             Vendedor                        Produto Data Venda  Total Vendas
# 18   Nicolas Pereira              Bermuda Masculino 2023-01-19       1039.92
# 8     Amanda Martins              Bermuda Masculino 2023-01-04       1485.60
# 14    Eliane Moreira              Bolsa de Trabalho 2023-01-08        994.92
# 3    Gabriel Cardoso                 Bota Masculina 2023-01-06        448.28
# 9   Leonardo Almeida                Calça Bailarina 2023-01-11        281.40
# 5     Eliane Moreira          Calça Feminina Jogger 2023-01-02        139.98
# 16    Carlos Moreira          Calça Feminina Jogger 2023-01-17        489.93
# 17    Eliane Moreira               Camisa Masculina 2023-01-18       1073.80
# 12   Nicolas Pereira               Camisa Masculina 2023-01-03        306.80
# 0       Paulo Santos  Camisa Masculina Festa Balada 2023-01-05        876.84
# 10    Eliane Moreira                 Camisa Térmica 2023-01-12         83.80
# 1     Eliane Moreira                 Colar Pingente 2023-01-15        719.20
# 13  Leonardo Almeida        Jaqueta Masculina Preta 2023-01-07        602.00
# 6    Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-01-09       1048.68
# 15    Amanda Martins               Sapatilha Sapato 2023-01-14        503.10
# 11   Nicolas Pereira                  Sapato Social 2023-01-13        573.30
# 2       Angela Maria                 Tênis Feminino 2023-01-16        359.96
# 4   Leonardo Almeida                 Tênis Feminino 2023-01-01        719.92
# 7     Amanda Martins               Vestido Infantil 2023-01-10         59.90

print("\n --------------------- Ordenando pela Data --------------------- \n")

ordenarDatas = vendas_DF.sort_values(by="Data Venda")

print(ordenarDatas)

#             Vendedor                        Produto Data Venda  Total Vendas
# 4   Leonardo Almeida                 Tênis Feminino 2023-01-01        719.92
# 5     Eliane Moreira          Calça Feminina Jogger 2023-01-02        139.98
# 12   Nicolas Pereira               Camisa Masculina 2023-01-03        306.80
# 8     Amanda Martins              Bermuda Masculino 2023-01-04       1485.60
# 0       Paulo Santos  Camisa Masculina Festa Balada 2023-01-05        876.84
# 3    Gabriel Cardoso                 Bota Masculina 2023-01-06        448.28
# 13  Leonardo Almeida        Jaqueta Masculina Preta 2023-01-07        602.00
# 14    Eliane Moreira              Bolsa de Trabalho 2023-01-08        994.92
# 6    Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-01-09       1048.68
# 7     Amanda Martins               Vestido Infantil 2023-01-10         59.90
# 9   Leonardo Almeida                Calça Bailarina 2023-01-11        281.40
# 10    Eliane Moreira                 Camisa Térmica 2023-01-12         83.80
# 11   Nicolas Pereira                  Sapato Social 2023-01-13        573.30
# 15    Amanda Martins               Sapatilha Sapato 2023-01-14        503.10
# 1     Eliane Moreira                 Colar Pingente 2023-01-15        719.20
# 2       Angela Maria                 Tênis Feminino 2023-01-16        359.96
# 16    Carlos Moreira          Calça Feminina Jogger 2023-01-17        489.93
# 17    Eliane Moreira               Camisa Masculina 2023-01-18       1073.80
# 18   Nicolas Pereira              Bermuda Masculino 2023-01-19       1039.92

print("\n --------------------- Ordenando pelo total de vendas --------------------- \n")

ordenarVendas = vendas_DF.sort_values(by="Total Vendas")

print(ordenarVendas)

#             Vendedor                        Produto Data Venda  Total Vendas
# 7     Amanda Martins               Vestido Infantil 2023-01-10         59.90
# 10    Eliane Moreira                 Camisa Térmica 2023-01-12         83.80
# 5     Eliane Moreira          Calça Feminina Jogger 2023-01-02        139.98
# 9   Leonardo Almeida                Calça Bailarina 2023-01-11        281.40
# 12   Nicolas Pereira               Camisa Masculina 2023-01-03        306.80
# 2       Angela Maria                 Tênis Feminino 2023-01-16        359.96
# 3    Gabriel Cardoso                 Bota Masculina 2023-01-06        448.28
# 16    Carlos Moreira          Calça Feminina Jogger 2023-01-17        489.93
# 15    Amanda Martins               Sapatilha Sapato 2023-01-14        503.10
# 11   Nicolas Pereira                  Sapato Social 2023-01-13        573.30
# 13  Leonardo Almeida        Jaqueta Masculina Preta 2023-01-07        602.00
# 1     Eliane Moreira                 Colar Pingente 2023-01-15        719.20
# 4   Leonardo Almeida                 Tênis Feminino 2023-01-01        719.92
# 0       Paulo Santos  Camisa Masculina Festa Balada 2023-01-05        876.84
# 14    Eliane Moreira              Bolsa de Trabalho 2023-01-08        994.92
# 18   Nicolas Pereira              Bermuda Masculino 2023-01-19       1039.92
# 6    Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-01-09       1048.68
# 17    Eliane Moreira               Camisa Masculina 2023-01-18       1073.80
# 8     Amanda Martins              Bermuda Masculino 2023-01-04       1485.60


print("\n --------------------- Ordenando por duas colunas (Vendedor e Produto) --------------------- \n")

ordenarDuasColunas = vendas_DF.sort_values(by=["Vendedor", "Produto"])

print(ordenarDuasColunas)

#             Vendedor                        Produto Data Venda  Total Vendas
# 8     Amanda Martins              Bermuda Masculino 2023-01-04       1485.60
# 15    Amanda Martins               Sapatilha Sapato 2023-01-14        503.10
# 7     Amanda Martins               Vestido Infantil 2023-01-10         59.90
# 2       Angela Maria                 Tênis Feminino 2023-01-16        359.96
# 16    Carlos Moreira          Calça Feminina Jogger 2023-01-17        489.93
# 14    Eliane Moreira              Bolsa de Trabalho 2023-01-08        994.92
# 5     Eliane Moreira          Calça Feminina Jogger 2023-01-02        139.98
# 17    Eliane Moreira               Camisa Masculina 2023-01-18       1073.80
# 10    Eliane Moreira                 Camisa Térmica 2023-01-12         83.80
# 1     Eliane Moreira                 Colar Pingente 2023-01-15        719.20
# 3    Gabriel Cardoso                 Bota Masculina 2023-01-06        448.28
# 9   Leonardo Almeida                Calça Bailarina 2023-01-11        281.40
# 13  Leonardo Almeida        Jaqueta Masculina Preta 2023-01-07        602.00
# 4   Leonardo Almeida                 Tênis Feminino 2023-01-01        719.92
# 18   Nicolas Pereira              Bermuda Masculino 2023-01-19       1039.92
# 12   Nicolas Pereira               Camisa Masculina 2023-01-03        306.80
# 6    Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-01-09       1048.68
# 11   Nicolas Pereira                  Sapato Social 2023-01-13        573.30
# 0       Paulo Santos  Camisa Masculina Festa Balada 2023-01-05        876.84

print("\n --------------------- Ordenando vendedor de Z a A --------------------- \n")

# ascending - False -> Z a A, - True -> A a Z
ordenaZaA = vendas_DF.sort_values(by="Vendedor", ascending=False)

print(ordenaZaA)

#             Vendedor                        Produto Data Venda  Total Vendas
# 0       Paulo Santos  Camisa Masculina Festa Balada 2023-01-05        876.84
# 6    Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-01-09       1048.68
# 12   Nicolas Pereira               Camisa Masculina 2023-01-03        306.80
# 11   Nicolas Pereira                  Sapato Social 2023-01-13        573.30
# 18   Nicolas Pereira              Bermuda Masculino 2023-01-19       1039.92
# 4   Leonardo Almeida                 Tênis Feminino 2023-01-01        719.92
# 13  Leonardo Almeida        Jaqueta Masculina Preta 2023-01-07        602.00
# 9   Leonardo Almeida                Calça Bailarina 2023-01-11        281.40
# 3    Gabriel Cardoso                 Bota Masculina 2023-01-06        448.28
# 5     Eliane Moreira          Calça Feminina Jogger 2023-01-02        139.98
# 1     Eliane Moreira                 Colar Pingente 2023-01-15        719.20
# 10    Eliane Moreira                 Camisa Térmica 2023-01-12         83.80
# 14    Eliane Moreira              Bolsa de Trabalho 2023-01-08        994.92
# 17    Eliane Moreira               Camisa Masculina 2023-01-18       1073.80
# 16    Carlos Moreira          Calça Feminina Jogger 2023-01-17        489.93
# 2       Angela Maria                 Tênis Feminino 2023-01-16        359.96
# 7     Amanda Martins               Vestido Infantil 2023-01-10         59.90
# 8     Amanda Martins              Bermuda Masculino 2023-01-04       1485.60
# 15    Amanda Martins               Sapatilha Sapato 2023-01-14        503.10

print("\n --------------------- Ordenando total vendas de Z a A --------------------- \n")

# ascending - False -> Z a A, - True -> A a Z
ordenaTotalVendasZaA = vendas_DF.sort_values(
    by="Total Vendas", ascending=False)

print(ordenaTotalVendasZaA)

#             Vendedor                        Produto Data Venda  Total Vendas
# 8     Amanda Martins              Bermuda Masculino 2023-01-04       1485.60
# 17    Eliane Moreira               Camisa Masculina 2023-01-18       1073.80
# 6    Nicolas Pereira    Kit de Pinceis de Maquiagem 2023-01-09       1048.68
# 18   Nicolas Pereira              Bermuda Masculino 2023-01-19       1039.92
# 14    Eliane Moreira              Bolsa de Trabalho 2023-01-08        994.92
# 0       Paulo Santos  Camisa Masculina Festa Balada 2023-01-05        876.84
# 4   Leonardo Almeida                 Tênis Feminino 2023-01-01        719.92
# 1     Eliane Moreira                 Colar Pingente 2023-01-15        719.20
# 13  Leonardo Almeida        Jaqueta Masculina Preta 2023-01-07        602.00
# 11   Nicolas Pereira                  Sapato Social 2023-01-13        573.30
# 15    Amanda Martins               Sapatilha Sapato 2023-01-14        503.10
# 16    Carlos Moreira          Calça Feminina Jogger 2023-01-17        489.93
# 3    Gabriel Cardoso                 Bota Masculina 2023-01-06        448.28
# 2       Angela Maria                 Tênis Feminino 2023-01-16        359.96
# 12   Nicolas Pereira               Camisa Masculina 2023-01-03        306.80
# 9   Leonardo Almeida                Calça Bailarina 2023-01-11        281.40
# 5     Eliane Moreira          Calça Feminina Jogger 2023-01-02        139.98
# 10    Eliane Moreira                 Camisa Térmica 2023-01-12         83.80
# 7     Amanda Martins               Vestido Infantil 2023-01-10         59.90
