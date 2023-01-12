import matplotlib.pyplot as plot
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

frutas = frutas_DF["Frutas"]
total = frutas_DF["Total Vendas"]

# plot = grafico de linhas
# label = Legenda
# linestyle = Estilo da linha - https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
# lw = Largura da linha
plot.plot(frutas_DF["Frutas"], frutas_DF["Total Vendas"],
          label="Total Vendas", linestyle="-", lw="2", color="g")
plot.legend()  # Exibe a legenda
plot.title("Vendas Frutas")  # Título
plot.xlabel("Nome das Frutas", size=20)  # Descrição eixo x
plot.ylabel("Total de Vendas", size=20)  # Descrição eixo y
plot.xticks([0, 1, 2, 3, 4])  # Escala de números eixo x
plot.yticks([0, 20, 40, 60, 80, 100])  # Escala de números eixo y
# Define o minimo e maximo para o eixo x e y
plot.axis(xmin=0, xmax=4, ymin=0, ymax=80)
plot.axis("auto")  # Ajusta o eixo x e y de forma automática
# grafico.annotate("Abacate", (0,10)) #Anotação
# grafico.annotate("Banana", (1,52)) #Anotação
plot.annotate(total[0], (frutas[0], total[0]))
plot.annotate(total[1], (frutas[1], total[1]))
plot.annotate(total[2], (frutas[2], total[2]))
plot.annotate(total[3], (frutas[3], total[3]))
plot.annotate(total[4], (frutas[4], total[4]))
plot.savefig("imagemGrafico.png")

# Cria e aprensenta o gráfico
plot.show()
