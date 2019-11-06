import pandas as pd 

file_01 = r'data/01. Viagens TIA.xls'
file_02 = r'data/02. Viagens TIA.xls'
file_03 = r'data/03. Viagens TIA.xls'
file_04 = r'data/04. Viagens TIA.xls'
file_05 = r'data/05. Viagens TIA.xls'
file_06 = r'data/06. Viagens TIA.xls'
file_07 = r'data/07. Viagens TIA.xls'
file_08 = r'data/08. Viagens TIA.xls'
file_09 = r'data/09. Viagens TIA.xls'

df_01 = pd.read_excel(file_01).iloc[2:]
df_02 = pd.read_excel(file_02).iloc[2:]
df_03 = pd.read_excel(file_03).iloc[2:]
df_04 = pd.read_excel(file_04).iloc[2:]
df_05 = pd.read_excel(file_05).iloc[2:]
df_06 = pd.read_excel(file_06).iloc[2:]
df_07 = pd.read_excel(file_07).iloc[2:]
df_08 = pd.read_excel(file_08).iloc[2:]
df_09 = pd.read_excel(file_09).iloc[2:]

result = pd.concat([df_01,df_02,df_03,
                   df_04,df_05,df_06,
                   df_07,df_08,df_09],join='outer',sort=True)


writer = pd.ExcelWriter('viagens_2019.xlsx')
result.to_excel(writer,'Sheet1',index=False)
writer.save()
# result.head()
