import csv
import pandas as pd

def file_save(row_list):
    headers = ['name','price','supplier','time']
    with open('./goods.csv', 'a' , newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, headers)
        #dict_writer.writeheader()        
        dict_writer.writerows(row_list)

def file_clean():
    df = pd.read_csv('./goods.csv', encoding='big5')
    df = df.drop_duplicates(subset=['name', 'price', 'supplier'], keep='last')
    df.to_csv('./goods.csv', encoding='big5', index=0)
    print('整理OK')