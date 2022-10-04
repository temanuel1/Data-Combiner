import os
import glob
import pandas as pd
os.chdir("C:/Users/tyler/APL Projects/Data Combiner/fishy files")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

def read(file):
    file_index = all_filenames.index(file) + 1
    print(f"Concating file {file} ({file_index}/{len(all_filenames)})")

    return pd.read_csv(file)

#combine all files in the list
combined_csv = pd.concat([read(f) for f in all_filenames ])

#export to csv
combined_csv.to_csv( "2020-2021(combined).csv", index=False, encoding='utf-8-sig')