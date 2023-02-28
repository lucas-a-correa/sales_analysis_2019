import pandas as pd
from datetime import datetime

#Função para limpar cada arquivo csv e salvar em um novo arquivo
def csv_cleaning(month):
    #lê o arquivo do mês escolhido
    csv = pd.read_csv(f'Sales_{month}_2019.csv')
    #elimina as linhas vazias
    csv = csv.dropna(how='all')
    #elimina as linhas com os títulos das colunas repetidos
    csv = csv[csv['Order ID'] != 'Order ID']
    #transforma a quantidade em numeral
    csv['Quantity Ordered'] = csv['Quantity Ordered'].apply(
        lambda x: int(x)
        )

    #transforma o preço em float
    csv['Price Each'] = csv['Price Each'].apply(
        lambda x: float(x)
        )

    #transforma a data de compra em datetime
    csv['Order Date'] = csv['Order Date'].apply(
        lambda x: datetime.strptime(x,'%m/%d/%y %H:%M')
        )

    #separa a string de cidade do endereço
    csv['City'] = csv['Purchase Address'].apply(
        lambda x: x.split(', ')[1]
        )

    #separa a string de estado do endereço
    csv['State'] = csv['Purchase Address'].apply(
        lambda x: x.split(', ')[2].split(' ')[0]
        )

    #separa a string de código postal do endereço
    csv['ZIP Code'] = csv['Purchase Address'].apply(
        lambda x: x.split(', ')[2].split(' ')[1]
        )
    #elimina a coluna original de endereço
    csv = csv.drop(['Purchase Address'], axis=1)
    
    #salva o csv limpo
    csv.to_csv(f'Sales_{month}_2019_clean.csv',index=False)
    
#lista de meses para acessar os arquivos
month_list = [
    'January','February','March','April','May','June','July','August',
    'September','October','November','December'
    ]

#aplica a função em cada arquivo
for month in month_list:
    csv_cleaning(month)

#cria um novo dataframe para realizar a fusão dos arquivos    
sales_2019 = pd.DataFrame()    

#lê cada arquivo e os funde no dataframe
for month in month_list:
    csv = pd.read_csv(f'Sales_{month}_2019_clean.csv')
    sales_2019 = pd.concat([sales_2019,csv])
  
#cria uma coluna com o preço*quantidade    
sales_2019['Total Price'] = sales_2019['Quantity Ordered']*sales_2019['Price Each']

#salva o arquivo csv
sales_2019.to_csv('sales_2019.csv',index=False)