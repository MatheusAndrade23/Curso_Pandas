import matplotlib.pyplot as pyplot
import pandas as pd

frutas_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Base_Grafico.xlsx')

print(frutas_DF)

#  DataFrame Frutas

#     Frutas  Total Vendas
# 0  Abacate            10
# 1   Banana            52
# 2   Goiaba            66
# 3  Laranja            99
# 4     Maça            13

# plot = grafico de linhas
pyplot.plot(frutas_DF["Frutas"], frutas_DF["Total Vendas"])
pyplot.title("Vendas Frutas")  # Título
pyplot.xlabel("Nome das Frutas")  # Descrição eixo x
pyplot.ylabel("Total de Vendas")  # Descrição eixo y

# Cria e aprensenta o gráfico
pyplot.show()
