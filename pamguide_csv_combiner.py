
import pandas as pd
import numpy as np
import os

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

# if not batches:...

csv_folder_path = './test_data/uncombined'

csv_names = os.listdir(csv_folder_path)
csv_names.sort()

def load_csvs(csv_names):
    csv_list = []

    i = -1
    for csv_name in csv_names:

        if csv_name[-4:] != '.csv':
            print(f'Skipping non-csv {csv_name}')
            continue

        i += 1

        print()
        csv = np.genfromtxt(f'{csv_folder_path}/{csv_name}', delimiter=',')
        print(f'CSV {i}')
        print('========================================')
        print(f'Name: {csv_name}')
        print(f'Size: {csv.size} rows, {csv[0].size} columns.')
        print(f'Start time: {csv[1][0]}')
        print(f'End time: {csv[-1][0]}')
        print(f'Duration: {csv[-1][0] - csv[1][0]}')

        if i != 0:
            csv = np.delete(csv, (0,), axis=0)
        csv_list.append(csv)

    print()
    return csv_list

csv_list = load_csvs(csv_names)
print(f'{len(csv_list)} CSVs loaded.')

combined_csv = np.vstack(csv_list)
print(f'Combined CSV numpy shape: {combined_csv.shape}')

save_path = './test_data/combined/combined_csv.csv'
print(f'CSV saved: {save_path}')
np.savetxt(save_path, combined_csv, delimiter=",")

