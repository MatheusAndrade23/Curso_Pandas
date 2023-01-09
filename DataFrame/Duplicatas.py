import pandas as pd

# Abrindo arquivo do Excel
vendas_DF = pd.read_excel(
    r'C:\Users\mathe\OneDrive\Área de Trabalho\curso_pandas\Planilhas\Base_Vendas.xlsx', engine="openpyxl")

print(vendas_DF)

#            Vendedor  Total Vendas
# 0    Amanda Martins       1485.60
# 1      Angela Maria        359.96
# 2    Carlos Moreira        489.93
# 3   Gabriel Cardoso        448.28
# 4   Gabriel Cardoso       1344.84
# 5  Leonardo Almeida        719.92
# 6   Nicolas Pereira        306.80
# 7   Nicolas Pereira       1048.68
# 8   Nicolas Pereira        573.30

print("\n --------------------- Imprimindo os dados únicos --------------------- \n")
resumoValoresUnicos = vendas_DF.nunique()

# filtra somente os valores unicos, conta este valores
print(resumoValoresUnicos)

# Vendedor        6
# Total Vendas    9
# dtype: int64


print("\n --------------------- Resumo das duplicidades --------------------- \n")

# subset = identifica a coluna em que queremos verificar a duplicidade
# keep = controle como considerar o valor da duplicidade = | first | last | false

confereDuplicidade = vendas_DF.duplicated(subset="Vendedor", keep="first")

print(confereDuplicidade)

# 0    False
# 1    False
# 2    False
# 3    False
# 4     True
# 5    False
# 6    False
# 7     True
# 8     True
# dtype: bool


print("\n --------------------- Nova coluna das informações duplicadas --------------------- \n")


vendas_DF["Confere Duplicidade"] = vendas_DF.duplicated(
    subset="Vendedor", keep="first")

print(vendas_DF)

#            Vendedor  Total Vendas  Confere Duplicidade
# 0    Amanda Martins       1485.60                False
# 1      Angela Maria        359.96                False
# 2    Carlos Moreira        489.93                False
# 3   Gabriel Cardoso        448.28                False
# 4   Gabriel Cardoso       1344.84                 True
# 5  Leonardo Almeida        719.92                False
# 6   Nicolas Pereira        306.80                False
# 7   Nicolas Pereira       1048.68                 True
# 8   Nicolas Pereira        573.30                 True

print("\n --------------------- Removendo as duplicidades --------------------- \n")

# removendo valores duplicados
removerDuplicidade = vendas_DF.drop_duplicates(subset="Vendedor", keep="first")

print(removerDuplicidade)

#            Vendedor  Total Vendas  Confere Duplicidade
# 0    Amanda Martins       1485.60                False
# 1      Angela Maria        359.96                False
# 2    Carlos Moreira        489.93                False
# 3   Gabriel Cardoso        448.28                False
# 5  Leonardo Almeida        719.92                False
# 6   Nicolas Pereira        306.80                False
