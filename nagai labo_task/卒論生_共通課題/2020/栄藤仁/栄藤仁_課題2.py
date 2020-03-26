#課題2_配布データ.csv

import os
import matplotlib.pyplot as plt


path = os.pardir

print(os.getcwd())
choice_address = path
processing_file = choice_address

want_files_name = []
input_name = input("名前を入力してください:")

for search_folder, search_sub_folders, search_files in os.walk(processing_file):
    for search_file in search_files:
        if search_file.count(input_name) > 0:
            want_files_name.append(os.path.join(search_folder,search_file))


I17_df = []
I18_df = []
I19_df = []

for want_file_name in want_files_name:
    with open(want_file_name. replace('\\','\\\\'), encoding = "shift-jis") as f:
        line = f.read().split('\n')
        for reader in line:
            if reader == line[0]:
                header = reader.split(',')
            else:
                row = reader.split(',')
                if not row[0]=="":
                    I17_df.append(int(row[0]))
                if not row[1]=="":
                    I18_df.append(int(row[1]))
                if not row[2]=="":
                    I19_df.append(int(row[2]))

points = (I17_df,I18_df,I19_df)
fig, ax = plt.subplots()

bp = ax.boxplot(points)
ax.set_xticklabels([header[0], header[1], header[2]])

plt.show()
