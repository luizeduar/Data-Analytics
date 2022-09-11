import pandas as pd
import os
import numpy as np
import math

path = 'C:\\Users\\laris\\OneDrive\\Documentos\\TAMBOR\\post_30'
os.chdir(path)

NP = 16638
NF = 100
r1 = 0.0009
r2 = 0.003
v1 = (4 / 3 * math.pi * r1 * r1 * r1)
v2 = (4 / 3 * math.pi * r2 * r2 * r2)

dados = []
delta = 0.02

Tipo = np.zeros((NP, NF))
dadosX = np.zeros((NP, NF))
dadosY = np.zeros((NP, NF))
dadosZ = np.zeros((NP, NF))
raio = np.zeros((NP, NF))
posicao_vetor = 1


listax = np.arange(-0.05,0.07,delta)
listay = np.arange(-0.05,0.07,delta)
listaz = np.arange(0,0.12,delta)
time =  np.arange(0,50.5,0.5)
posicao = np.arange(0,125,1)
rx = 5
ry = 5
rz = 5
tamanho = rx * ry * rz - 1

contador_tipo1 = pd.DataFrame(np.zeros((tamanho, NF)))
contador_tipo2 = pd.DataFrame(np.zeros((tamanho, NF)))

for j in range(NF):
    Dados = pd.read_csv('data_{}.csv'.format(j))
    Tipo[:, j] = Dados.iloc[:, 2-1].copy()
    raio[:, j] = Dados.iloc[:, 6-1].copy()
    dadosX[:, j] = Dados.iloc[:, 7-1].copy()
    dadosY[:, j] = Dados.iloc[:, 8-1].copy()
    dadosZ[:, j] = Dados.iloc[:, 9-1].copy()

raio = pd.DataFrame(raio)
volume = (4 / 3 * math.pi * raio * raio * raio)
dadosX = pd.DataFrame(dadosX)
dadosY = pd.DataFrame(dadosY)
dadosZ = pd.DataFrame(dadosZ)
Tipo = pd.DataFrame(Tipo)

for m in range(NF):
    print(int(m/NF*100))
    for n in range(NP):
        if Tipo.iloc[n, m] < 1.5:
            px = round(dadosX.iloc[n, m] / delta +3)
            py = round(dadosY.iloc[n, m] / delta +3)
            pz = np.ceil(dadosZ.iloc[n, m] / delta )
            posicao_vetor = int( -31 + px + 5 * py + 25 * pz)
            contador_tipo1.iloc[posicao_vetor, m] = contador_tipo1.iloc[posicao_vetor, m] + 1
        else:
            contador_tipo2.iloc[posicao_vetor, m] = contador_tipo2.iloc[posicao_vetor, m] + 1


volume1 = contador_tipo1*v1
volume2 = contador_tipo2*v2
C1 = volume1/(volume1+volume2)
desvio = np.std(C1)
indice = pd.DataFrame(desvio)
path = 'C:\\Users\\laris\\OneDrive\\Documentos\\TAMBOR\\Tratados'
os.chdir(path)
indice.to_csv('data30.csv')
