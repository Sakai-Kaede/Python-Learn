### if文について ###

# 以下の場合はFalseと評価される
# None False 数値の0 空のオブジェクト Falseを返すオブジェクト lenが0を返すオブジェクト

# 上記以外は全てTrueと評価される

# 例えば、オブジェクトの真理値判定に利用可能
def first_item(items):
  if len(items):
    return items[0]
  else:
    return None
  
print(first_item(['book'])) # [book]と表示される
print(first_item([])) # [None]と表示される

# ある要素がコンテナオブジェクトに含まれるか判定
count = {'book': 1, 'note': 2}
print('book' in count) # [True]と表示される


### ループについて ###

# for文は変数のスコープをブロック内に限定しない
i = 100
for i in range(3):
  pass

print(i) # 2と表示される

# ↑ ループで使う変数名を(_)で統一しておくと、変数名が被ること問題を軽減できる


### 例外処理について ###

# try文を利用すると強制終了を避けられる

def get_book(index):
  items = ['note', 'notebook', 'sketchbook']
  try:
    return items[index]
  except IndexError:
    return '範囲外です'
  
get_book(10) # [範囲外です]と表示される

## 補足 ## except節は複数記述できる

# else節を使ってtryブロックを小さくすることで
# 例外が発生する可能性のある処理が明確になる

def get_book_upper(index):
  items = ['note', 'notebook', 'sketchbook']
  try:
    book = str(items[index])
    # return book.upper() else節へ移動する
  except (IndexError, TypeError) as e:
    print(f'例外が発生しました: {e}')
  else:
    return book.upper()

# finally節は例外の発生有無にかかわらずtryブロックを
# 抜ける際に必ず実行される

f = open('some.txt', 'r')
try:
  print(f.read())
finally:
  f.close()

# with文は事前に定義されているクリーンアップ処理を利用する

with open('some.txt', 'w') as f:
  f.write('some text')

print(f.closed)