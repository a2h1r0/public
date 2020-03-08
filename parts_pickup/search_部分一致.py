import pandas as pd

    
## データの読み込み ##
filename = 'data.csv' # ファイル名
# ファイル名.read_csvで読み込む
# "Python read_csv"で検索
datafile = pd.read_csv(filename, usecols=['製品番号', '分類', 'サイズ', '単価', '在庫数'], encoding='Shift-JIS')

print('\n↓検索カテゴリ一覧↓')
print(['製品番号', '分類', 'サイズ', '単価', '在庫数'])

# "Python input"で検索
strinput = input('\n検索カテゴリを入力してください： ')
# ファイル名.columns.get_loc(文字列)で検索するカテゴリの列番号を保存
# "Python get_loc"で検索
category = datafile.columns.get_loc(strinput)

search = input('検索ワードを入力してください： ')


# "Python itertuples"で検索
for row in datafile.itertuples(name=None):   ## データを1行ずつ読み出し:
    
    # もし取り出した行の検索カテゴリの値に，検索ワードが含まれていたら
    if search in row[category+1]:
        # その行を表示する
        print(row)
        
"""
ちなみに，出てきた値が(6, 'SGK2R2G4', '小なべネジ', 'M8', 19, 4532)のように
1列目に番号が振られているため(Dataflameの特徴("Python Dataflame"で検索))，
if search in row[category+1]:
この文のrow[category+1]は+1している．
"""