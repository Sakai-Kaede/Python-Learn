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
  
print(first_item(['book'])) # bookと表示される
print(first_item([])) # Noneと表示される