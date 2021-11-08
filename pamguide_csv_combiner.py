
import pandas as pd
import numpy as np
import os


debug = False

print(
        '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ____  ___    __  _________      _     __        ____________    __   ______                __    _                
   / __ \/   |  /  |/  / ____/_  __(_)___/ /__     / ____/ ___/ |  / /  / ____/___  ____ ___  / /_  (_)___  ___  _____
  / /_/ / /| | / /|_/ / / __/ / / / / __  / _ \   / /    \__ \| | / /  / /   / __ \/ __ `__ \/ __ \/ / __ \/ _ \/ ___/
 / ____/ ___ |/ /  / / /_/ / /_/ / / /_/ /  __/  / /___ ___/ /| |/ /  / /___/ /_/ / / / / / / /_/ / / / / /  __/ /    
/_/   /_/  |_/_/  /_/\____/\__,_/_/\__,_/\___/   \____//____/ |___/   \____/\____/_/ /_/ /_/_.___/_/_/ /_/\___/_/     

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''')

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

def load_csvs(csv_names):
    csv_list = []

    i = 0
    for csv_name in csv_names:

        if csv_name[-4:] != '.csv':
            #if debug:
            print(f'Skipping non-csv {csv_name}')
            continue

        i += 1

        csv = np.genfromtxt(csv_name, delimiter=',')

        if debug:
            print()
            print(f'CSV {i}')
            print('========================================')
            print(f'Name: {csv_name}')
            print(f'Size: {csv.size} rows, {csv[0].size} columns.')
            print(f'Start time: {csv[1][0]}')
            print(f'End time: {csv[-1][0]}')
            print(f'Duration: {csv[-1][0] - csv[1][0]}')

        if i != 1:
            csv = np.delete(csv, (0,), axis=0)
        csv_list.append(csv)

    print()
    return csv_list

csv_list = load_csvs(csv_names)
print(f'{len(csv_list)} CSVs loaded.')

combined_csv = np.vstack(csv_list)
print(f'Combined CSV numpy shape: {combined_csv.shape}')

if not os.path.exists('./combined'):
    os.makedirs('./combined')

print('Enter CSV name without file ending.')
file_name = input('>>> ')
if file_name == '':
    file_name = 'combined_csv'
save_path = f'./combined/{file_name}.csv'

print(f'Saving csv: {save_path}')
np.savetxt(save_path, combined_csv, delimiter=",")

