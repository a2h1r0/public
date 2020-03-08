import pandas as pd
import csv

    
filename = 'data_plus.csv'
datafile = pd.read_csv(filename, usecols=['製品番号', '分類', 'サイズ', '単価', '在庫数', '製造元'], encoding='Shift-JIS')

print('\n↓検索カテゴリ一覧↓')
print(['製品番号', '分類', 'サイズ', '単価', '在庫数', '製造元'])

strinput = input('\n検索カテゴリを入力してください： ')
category = datafile.columns.get_loc(strinput)
search = input('検索ワードを入力してください： ')


# ファイルをオープンする．"Python csv 書き込み"で検索
with open('output.csv', 'a', newline="") as f: # 変更点
    writer = csv.writer(f) # 変更点
    
    # ヘッダー(行のタイトルのこと)を書き込んであげる
    writer.writerow(['製品番号', '分類', 'サイズ', '単価', '在庫数', '製造元']) # 変更点
    for row in datafile.itertuples(name=None):
        if search in row[category+1]:
            print(row)
                        
            # 検索して一致した結果をファイルに書き込む
            writer.writerow(row[1:]) # 変更点

        
"""
先述の通り，(6, 'SGK2R2G4', '小なべネジ', 'M8', 19, 4532)のように1列目には番号が振られている．
そのためwriter.writerow(row[1:])はrow[1:]としている．
これで1列目(最初の数字は0列目)から最後までを取り出している．
"Python スライス"で検索．

ただ，これだと実行ごとに毎回ヘッダーが書き込まれるので，追記するなら処理が必要．
具体的にはif文で，ファイルが存在するならヘッダーを書き込まず，存在しなければ書き込む．
"Python os isfile"で検索．
"""