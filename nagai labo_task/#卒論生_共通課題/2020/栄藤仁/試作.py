#課題2_配布データ.csv

import os
import matplotlib.pyplot as plt

'''
path = os.getcwd()
path = os.pardir
'''
print(os.getcwd())
choice_address = "/Users/etojin/anaconda3/bin/conda/nagai labo_task/#卒論生_共通課題/2020"
processing_file = choice_address

want_files_name=[]
input_name=input("名前を入力してください:")
print(input_name)
for search_folder, search_subfolders, search_files in os.walk(processing_file):
    for search_file in search_files:
        if search_file.count(input_name)>0:
            want_files_name.append(os.path.join(search_folder,search_file))
print(want_files_name)
print(len(want_files_name))

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
print(I18_df)

I17_df.sort()
I18_df.sort()
I19_df.sort()
print(I17_df)
print(I18_df)
print(I19_df)
#print(I17_df[int(int(len(I17_df)) / 4)+10])
'''
if int(len(I17_df)) % 2 == 0:
    print(I17_df[int(int(len(I17_df)) / 2)])

else:
    print(int((I17_df[int(int(len(I17_df)) / 2)+1]+I17_df[int(int(len(I17_df)) / 2)-1])/2))
'''


plot = (I17_df,I18_df,I19_df)
fig, ax = plt.subplots()

bp = ax.boxplot(plot)
ax.set_xticklabels(['I17_df', 'I18_df','I19_df'])
'''
plt.title('Titke')
plt.xlabel('Xlabel')
plt.ylabel('Ylabel')
# Y軸のメモリのrange
plt.ylim([1900,5700])
plt.grid()
'''
# 描画
plt.show()
#print(int(int(len(I17_df)) / 4))
