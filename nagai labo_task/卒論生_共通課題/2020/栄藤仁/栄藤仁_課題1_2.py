import os
# osを使用

import pandas as pd
# pandas(ライブラリソフト)を使用、以後pandasをpdで表す

path = os.getcwd()
print("絶対パス:", path, "\n")
# python 実行しているディレクトリの絶対パス取り出し

path = os.pardir
# 1つ前のdirectoryのpathを取得

file_names = os.listdir(path)
file_names.sort()
# file_names で取り出したリストを五十音順に並び替え
print("ファイルたち:", file_names, "\n")
# 出力	['Pythonプログラミング課題.pdf', 'load_excel.py', '~$課題1_配布データ.xlsx', '課題1_配布データ.xlsx', '課題2_配布データ.csv']

pattern = '課題1'
ext = 'xlsx'
want_file_name = ""
print("for loop 入るよ\n")
for v in file_names:
	print(v)
	# vはそのファイルの中の全てを対象
	if v.startswith(pattern) and v.endswith(ext) and '$' not in v:
		want_file_name = v
		break
print("for loop 出たよ\n")
# 「課題 ~」、「.xlsx」 で始まるファイルを取り出し
# 「$」入りは選択しない

df = pd.read_excel(os.path.join(path, want_file_name))
# 変数 path と変数 file_names のパスを連結させて、それを読み込み
print(df)

l = []
if l:
	print ('not empty')
else:
	print('empty')
# 空のファイルを作成

for deta in df['実績(万kW)']:
    if deta >= 4000:
       l.append(deta)
		# appendは末尾に要素を追加
print(l)
# l(空のファイルに4000よりでかいデータのみを追加
df2 = pd.DataFrame(l,columns=['実績(万kW)'])
# columns列名index行名で、列名を'実績(万kW)'にしてpandas.DataFrame構造に整列
print(df2)

df2.to_csv('栄藤仁_課題1_result.csv',index =False, encoding = "shift-jis")
# index行頭全てを書き出さず、encodeを"shift-jis"の形でcsvファイルとして書き出し