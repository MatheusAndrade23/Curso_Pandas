import matplotlib.pyplot as plot
import pandas as pd

frutas_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Base_Grafico.xlsx')

print(frutas_DF)

#     Frutas  Total Vendas
# 0  Abacate            10
# 1   Banana            52
# 2   Goiaba            66
# 3  Laranja            99
# 4     Maça            13

# Tamanho da figura podemos aumentar ou diminuir
figura = plot.figure(figsize=(40, 20))

frutas = frutas_DF["Frutas"]
total = frutas_DF["Total Vendas"]

# 2 = linha, 3 = colunas, 1 = posição do grafico
# add_subplot = Adiciona um gráfico na parte de uma figura
figura.add_subplot(231)
plot.plot(frutas, total, label="plot")
plot.legend()
plot.title("Gráfico 1")
plot.annotate(frutas[0], (frutas[0], total[0]))
plot.annotate(frutas[1], (frutas[1], total[1]))
plot.annotate(frutas[2], (frutas[2], total[2]))
plot.annotate(frutas[3], (frutas[3], total[3]))
plot.annotate(frutas[4], (frutas[4], total[4]))
plot.xticks([])

# 2 = linha, 3 = colunas, 2 = posição do grafico
# add_subplot = Adiciona um gráfico na parte de uma figura
figura.add_subplot(232)
plot.bar(frutas, total, label="bar")
plot.legend()
plot.title("Gráfico 2")
plot.annotate(frutas[0], (frutas[0], total[0]))
plot.annotate(frutas[1], (frutas[1], total[1]))
plot.annotate(frutas[2], (frutas[2], total[2]))
plot.annotate(frutas[3], (frutas[3], total[3]))
plot.annotate(frutas[4], (frutas[4], total[4]))
plot.xticks([])


# 1 = linha, 3 = colunas, 3 = posição do grafico
# add_subplot = Adiciona um gráfico na parte de uma figura
figura.add_subplot(233)
plot.pie(total, labels=frutas)
plot.title("Gráfico 3")


# 2 = linha, 3 = colunas, 5 = posição do grafico
# add_subplot = Adiciona um gráfico na parte de uma figura
figura.add_subplot(235)
plot.stem(frutas, total, label="stem")
plot.legend()
plot.title("Gráfico 4")
plot.annotate(frutas[0], (frutas[0], total[0]))
plot.annotate(frutas[1], (frutas[1], total[1]))
plot.annotate(frutas[2], (frutas[2], total[2]))
plot.annotate(frutas[3], (frutas[3], total[3]))
plot.annotate(frutas[4], (frutas[4], total[4]))
plot.xticks([])

plot.savefig("figuraGrafico.png")

plot.show()
