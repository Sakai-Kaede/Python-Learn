# コメント文は「#」をつけることで書ける
# 関数などの説明文は「"""」をつけることで書ける(docstring)

# 以下にdocstringの例を示す

def sum(num1, num2):
    """
    概要
        2つの数値を足し合わせる関数です。

    詳細説明
        この関数は、2つの数値を受け取り、それらを足し合わせた結果を返します。数値は整数または浮動小数点数である必要があります。

    Args:
        num1 (int, float): 最初の数値
        num2 (int, float): 2番目の数値

    Returns:
        int, float: 2つの入力数値を足した結果

    Raises:
        TypeError: 引数が数値でない場合に発生します

    Examples:

        関数の使い方

        >>> sum(5, 6)
        11
        >>> sum(3.5, 2.5)
        6.0

    Note:
        引数は整数または浮動小数点数である必要があります。
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("引数は整数または浮動小数点数である必要があります。")
    return num1 + num2

print(sum(5, 6)) # 11と表示される
print(sum(3.5, 2.5)) # 6.0と表示される
