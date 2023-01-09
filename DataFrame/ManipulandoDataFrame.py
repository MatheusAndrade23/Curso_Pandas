import numpy as np
import pandas as pd

print("\n --------------------- DataFrame Dicionário NotasAlunos --------------------- \n")

notasAlunos = {
    "Nome": ['Ana', 'Pedro', 'João'],
    "Nota 1": [9, 7, 10],
    "Nota 2": [7, 4, 8],
    "Nota 3": [5, 7, 0],
    "Nota 4": [6, 7, 7]
}

notasAlunos_DF = pd.DataFrame(notasAlunos)

print(notasAlunos_DF)

#     Nome  Nota 1  Nota 2  Nota 3  Nota 4
# 0    Ana       9       7       5       6
# 1  Pedro       7       4       7       7
# 2   João      10       8       0       7

print("\n --------------------- DataFrame Dicionário NotasAlunos com a média calculada e adicionada --------------------- \n")

notasAlunos_DF['Média'] = (notasAlunos_DF["Nota 1"] + notasAlunos_DF["Nota 2"] +
                           notasAlunos_DF["Nota 3"] + notasAlunos_DF["Nota 4"]) / 4

print(notasAlunos_DF)

#     Nome  Nota 1  Nota 2  Nota 3  Nota 4  Média
# 0    Ana       9       7       5       6   6.75
# 1  Pedro       7       4       7       7   6.25
# 2   João      10       8       0       7   6.25

print("\n --------------------- DataFrame Dicionário NotasAlunos com coluna de faltas com valor padrão --------------------- \n")

notasAlunos_DF['Faltas'] = 5
print(notasAlunos_DF)

#     Nome  Nota 1  Nota 2  Nota 3  Nota 4  Média  Faltas
# 0    Ana       9       7       5       6   6.75       5
# 1  Pedro       7       4       7       7   6.25       5
# 2   João      10       8       0       7   6.25       5

print("\n --------------------- DataFrame Dicionário NotasAlunos com coluna de faltas com valores substituídos com uma lista --------------------- \n")


novasFaltas = [2, 3, 5]

notasAlunos_DF["Faltas"] = novasFaltas
print(notasAlunos_DF)

#     Nome  Nota 1  Nota 2  Nota 3  Nota 4  Média  Faltas
# 0    Ana       9       7       5       6   6.75       2
# 1  Pedro       7       4       7       7   6.25       3
# 2   João      10       8       0       7   6.25       5

# ---------------------------------------------------------------------------------

print("\n --------------------- Alterando a Nota 2 do aluno Pedro --------------------- \n")

# loc = localizar

notasAlunos_DF.loc[1, "Nota 2"] = 12
print(notasAlunos_DF)

#     Nome  Nota 1  Nota 2  Nota 3  Nota 4  Média  Faltas
# 0    Ana       9       7       5       6   6.75       2
# 1  Pedro       7      12       7       7   6.25       3
# 2   João      10       8       0       7   6.25       5

print("\n --------------------- Recalculando Média --------------------- \n")

notasAlunos_DF['Média'] = (notasAlunos_DF["Nota 1"] + notasAlunos_DF["Nota 2"] +
                           notasAlunos_DF["Nota 3"] + notasAlunos_DF["Nota 4"]) / 4

print(notasAlunos_DF)

#     Nome  Nota 1  Nota 2  Nota 3  Nota 4  Média  Faltas
# 0    Ana       9       7       5       6   6.75       2
# 1  Pedro       7      12       7       7   8.25       3
# 2   João      10       8       0       7   6.25       5
