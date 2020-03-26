import os
# osを使用

import pandas as pd
# pandas(ライブラリソフト)を使用

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

