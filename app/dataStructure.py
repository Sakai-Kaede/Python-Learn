### Noneについて ###

# Noneはシングルトンの性質をもつ
# 判定の際は、オブジェクトIDを確認するis、is notを使う

n = None
if n is None:
  print('nの値はNoneです')
else:
  print('nの値はNoneではありません')
# [nの値はNoneです]と表示される


### 配列について ###

# list型

# 要素の追加と削除
items = ['note', 'notebook', 'sketchbook']
items.append('paperbook')
print(items) # ['note', 'notebook', 'sketchbook', 'paperbook']と表示される

items = ['book'] + items
print(items) # ['book', 'note', 'notebook', 'sketchbook', 'paperbook']と表示される

items.pop(0)
print(items) # ['note', 'notebook', 'sketchbook', 'paperbook']と表示される

del items[1]
print(items)# ['note', 'sketchbook', 'paperbook']と表示される

# tuple型

# tuple型は定義後に要素を変更できない
items = ('note', 'notebook', 'sketchbook')

# listとtupleの使い分け

# アプリケーション内の設定値など作成時の組み合わせが変化しないものはtupleを使う