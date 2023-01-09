import numpy as np
import pandas as pd

# date_range = cria uma lista
# periods = quantos dias
# 20230101 = Ano/Mes/dia

dataFrame_Datas_Dias = pd.date_range('20230101', periods=31)

print(dataFrame_Datas_Dias)

# DatetimeIndex(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',
#                '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08',
#                '2023-01-09', '2023-01-10', '2023-01-11', '2023-01-12',
#                '2023-01-13', '2023-01-14', '2023-01-15', '2023-01-16',
#                '2023-01-17', '2023-01-18', '2023-01-19', '2023-01-20',
#                '2023-01-21', '2023-01-22', '2023-01-23', '2023-01-24',
#                '2023-01-25', '2023-01-26', '2023-01-27', '2023-01-28',
#                '2023-01-29', '2023-01-30', '2023-01-31'],
#               dtype='datetime64[ns]', freq='D')

print("\n --------------------- DataFrame 12 meses com a freq M --------------------- \n")

dataFrame_Datas_Meses = pd.date_range('20230101', periods=12, freq="M")

# freq = frequência -> 'M', 'Y'

print(dataFrame_Datas_Meses)

# DatetimeIndex(['2023-01-31', '2023-02-28', '2023-03-31', '2023-04-30',
#                '2023-05-31', '2023-06-30', '2023-07-31', '2023-08-31',
#                '2023-09-30', '2023-10-31', '2023-11-30', '2023-12-31'],
#               dtype='datetime64[ns]', freq='M')


print("\n --------------------- DataFrame com números aleatórios-> 5 linhas e 1 coluna --------------------- \n")

numerosAleatorios = pd.DataFrame(np.random.rand(5, 1))

print(numerosAleatorios)

# 1  0.896177
# 2  0.904997
# 3  0.022424
# 4  0.883211

print("\n --------------------- DataFrame com números aleatórios-> 15 linhas e 10 colunas --------------------- \n")

numerosAleatorios = pd.DataFrame(np.random.rand(15, 10))

print(numerosAleatorios)

#            0         1         2         3         4         5         6         7         8         9
# 0   0.942415  0.460800  0.269045  0.748643  0.127294  0.052941  0.490157  0.543915  0.615951  0.885760
# 1   0.325621  0.596322  0.621764  0.991167  0.702661  0.098543  0.181151  0.126972  0.912753  0.865859
# 2   0.233895  0.642355  0.715083  0.404607  0.566000  0.182547  0.133291  0.088033  0.997718  0.645796
# 3   0.183858  0.630993  0.920831  0.649238  0.972668  0.835153  0.957861  0.411695  0.836687  0.013516
# 4   0.929395  0.795654  0.486548  0.004329  0.804417  0.484454  0.616165  0.979021  0.154437  0.144797
# 5   0.979917  0.265764  0.631382  0.990852  0.504925  0.474429  0.376879  0.695222  0.387557  0.578313
# 6   0.210286  0.357013  0.886994  0.709954  0.367264  0.425485  0.839724  0.659704  0.745352  0.642146
# 7   0.691946  0.764618  0.049785  0.109344  0.734387  0.390746  0.103685  0.263426  0.014084  0.027444
# 8   0.800434  0.312515  0.087058  0.132055  0.490151  0.484897  0.237488  0.324926  0.533083  0.935502
# 9   0.460732  0.433501  0.046354  0.415999  0.168504  0.969601  0.425486  0.115064  0.153008  0.015240
# 10  0.251348  0.913148  0.731101  0.645079  0.798483  0.071219  0.728820  0.051946  0.532893  0.810274
# 11  0.386311  0.033074  0.402402  0.368496  0.134437  0.490558  0.506454  0.580698  0.315518  0.132817
# 12  0.832257  0.569449  0.285314  0.778859  0.377782  0.077108  0.425813  0.016682  0.020738  0.189157
# 13  0.619083  0.288704  0.662831  0.713354  0.585606  0.339082  0.709415  0.971409  0.570844  0.124654
# 14  0.742984  0.501206  0.766188  0.895688  0.249323  0.289793  0.782272  0.639475  0.189186  0.190058