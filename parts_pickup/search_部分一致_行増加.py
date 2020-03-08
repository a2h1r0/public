import pandas as pd

    
filename = 'data_plus.csv' # 変更点
datafile = pd.read_csv(filename, usecols=['製品番号', '分類', 'サイズ', '単価', '在庫数', '製造元'], encoding='Shift-JIS') # 変更点

print('\n↓検索カテゴリ一覧↓')
print(['製品番号', '分類', 'サイズ', '単価', '在庫数', '製造元'])

strinput = input('\n検索カテゴリを入力してください： ')
category = datafile.columns.get_loc(strinput)
search = input('検索ワードを入力してください： ')


for row in datafile.itertuples(name=None):    
    if search in row[category+1]:
        print(row)
