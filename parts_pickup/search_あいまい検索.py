import pandas as pd

    
## データの読み込み ##
filename = 'data.csv' # ファイル名
datafile = pd.read_csv(filename, usecols=['製品番号', '分類', 'サイズ', '単価', '在庫数'], encoding='Shift-JIS')
error_size = 2  # 何文字まで曖昧を許容するか

print('\n↓検索カテゴリ一覧↓')
print(['製品番号', '分類', 'サイズ', '単価', '在庫数'])
category = datafile.columns.get_loc(input('\n検索カテゴリを入力してください： '))+1  # ジャンルを列番号として保存
search = input('検索ワードを入力してください： ')

# 検索ワードが曖昧許容文字数より小さいとおかしくなるので回避
if len(search) <= error_size:
    step = error_size
# 検索ワードの文字列から曖昧許容文字列を引いて探していく
else:
    step = len(search)-error_size

for row in datafile.itertuples(name=None):   ## データを1行ずつ読み出し:
    # 完全一致
    # 1行のデータのカテゴリで指定した要素が検索ワードの文字列を含んでいれば出力
    if search in row[category]:
        print(row)
        # continueを入れないとあいまい検索でもう一回引っかかる
        continue

    # あいまい検索
    # 検索ワードの文字列をstep文字ずつ取り出していく
    for start in range(len(list(search))):
        c = search[start:start+step]
        # 検索文字列の最後まで確認したら終了(これがないと1文字になるまで検索してしまう)
        if len(search) < start+step:
            break
        # あいまい検索なので，小文字大文字の区別なく比較
        if c.lower() in row[category].lower():
            # "*"マークを表示してあげる
            print('*', end='')
            print(row)
            # 一致部分があれば終了(2回以上出力されてしまう場合があるので)
            break