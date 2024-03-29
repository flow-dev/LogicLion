N = int(input())
A = list(map(int, input().split()))

"""
このコードは、Pythonのプログラムで、ユーザーからの入力を受け取り、それを整数のリストに変換しています。具体的には、以下の手順で動作します。

1. `input()` 関数を使ってユーザーに入力を促します。ユーザーはスペースで区切られた整数を入力する必要があります。

2. `input()` で受け取った文字列を `split()` メソッドを使ってスペースで分割します。これにより、入力された文字列が整数のリストに変換されます。

3. `map(int, ...)` を使って、分割された各要素を整数に変換します。`map()` 関数は、指定された関数（この場合は `int`）をシーケンスの各要素に適用します。

4. `list(...)` で、変換された整数を含むリストを作成します。これにより、変数 `A` に整数のリストが格納されます。

例えば、ユーザーが "1 2 3" と入力した場合、変数 `A` は `[1, 2, 3]` となります。
"""

mn = min(A)
mx = max(A)

for a in A:
    print(max(a - mn, mx - a))