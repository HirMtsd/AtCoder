# coding: utf-8
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 421-A'
# 2025/09/01

# 実際の処理
def func(n, s, x, y):
    # 答は"Yes"か"No"なので、最初に"No"を設定
    ans = "No"
    
    # s[x-1]とyを比較
    if s[x-1] == y:
        ans = "Yes"

    # 答えを返す
    return(ans)

# このプログラムを直接呼び出した場合
# (テストのときに画面からの入力と、画面への出力を行わないようにするための機構)
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を1つの数値として扱う(入力は1～100に限定されている。)
    n = int(input())
    # 2～n+1行目の入力をn個の文字列リストとして扱う(文字列長は1～10に限定されている。)
    s = [""]*n
    for i in range(n):
        s[i] = input()
    # n+2行目の入力を2つの文字列として扱う
    x_s,y = input().split()
    # 1文字目を整数とする
    x = int(x_s)
    
    # 処理を呼び出し、結果を出力する
    print(func(n, s, x, y))

