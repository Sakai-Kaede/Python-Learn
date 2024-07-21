### Noneについて ###

# Noneはシングルトンの性質をもつ
# 判定の際は、オブジェクトIDを確認するis、is notを使う

n = None
if n is None:
  print('nの値はNoneです')
else:
  print('nの値はNoneではありません')
# [nの値はNoneです]と表示される
