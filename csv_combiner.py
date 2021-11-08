
import pandas as pd
import numpy as np
import os


debug = False

print('Enter parent CSV folder. CSVs in this folder and subdirectories  will be read and combined to a new file.')
csv_folder_path = input('>>> ')
if csv_folder_path == '':
    #csv_folder_path = '/Users/georgeamccarthy/Documents/MPhysProject/AcousticData/CambridgeBay_201901/'
    csv_folder_path = '/Users/georgeamccarthy/Documents/MPhysProject/AcousticData/CambridgeBay_201903/'

csv_names = []
for root, dirs, files in os.walk(csv_folder_path):
    for file in files:
        if file.endswith(".csv"):
            csv_names.append(os.path.join(root, file))

csv_names.sort()

df_from_each_csv = (pd.read_csv(f) for f in csv_names)
concatenated_df = pd.concat(df_from_each_csv)

if not os.path.exists('./combined'):
    os.makedirs('./combined')

print('Enter CSV name without file ending.')
file_name = input('>>> ')
if file_name == '':
    file_name = 'combined_csv'
save_path = f'./combined/{file_name}.csv'

print(f'Saving csv: {save_path}')
concatenated_df.to_csv(save_path, index=False)

