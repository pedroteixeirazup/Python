import matplotlib.pyplot as plt
from pandas import DataFrame, read_csv, ExcelFile, ExcelWriter
from datetime import datetime
import pandas as pd

def df_hours(hora_prevista, hora_entreposto):
    
    if hora_entreposto > hora_prevista:
        
        dif = hora_entreposto - hora_prevista
        dif_in_s = dif.total_seconds()
        dias = divmod(dif_in_s,86400)
        horas = divmod(dias[1],3600)
        minutos = divmod(horas[1],60)
        segundos = divmod(minutos[1],1)

        if horas[0] >= 1 and minutos[0] >= 1:
            return 'ATRASADO'
        else: 
            return 'SEM ATRASO'
    else :
        return 'SEM ATRASO'

def reader():
    file = r'data/viagens.xls'
    df = pd.read_excel(file)
    chegada_prevista, chegada_entreposto =  df['Chegada Prevista'], df['Chegada ao Entreposto']
    lenght = len(chegada_prevista)

    atrasado = list()
    sem_atraso = list()

    
    for i in range(lenght):

        if pd.isna(chegada_prevista[i]):
            continue
        else:
            data_prevista = str(chegada_prevista[i]).split(' ')
            datap = data_prevista[1]
            time_prevista = datetime.strptime(datap, '%H:%M:%S')

        
        if pd.isna(chegada_entreposto[i]):
            continue
        else:
            data_entreposto = str(chegada_entreposto[i]).split(' ') 
            datae = data_entreposto[1]
            time_entreposto = datetime.strptime(datae, '%H:%M:%S')
        
        aux = df_hours(time_entreposto, time_prevista)
        if aux == 'ATRASADO':
            atrasado.append(aux)
        else:
            sem_atraso.append(aux)
            
    return atrasado, sem_atraso


atrasado, sem_atraso = reader()

labels = 'ATRASADO', 'SEM ATRASO'
sizes = [len(atrasado), len(sem_atraso)]
explode = (0,0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
ax1.axis('equal')

plt.show()