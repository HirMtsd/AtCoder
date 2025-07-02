# coding: utf-8
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 409-A'
# 2025/07/02

# 実際の処理
def func(n, t, a):
    # ここにロジックを書く
    # 答は"Yes"か"No"なので、最初に"No"を設定
    ans = "No"

    # n回ループ処理
    for i in range(n):
        # 文字列tと文字列aのi番目を比較し、両方"o"なら、ansを"Yes"にして離脱
        if t[i] == "o" and t[i] == a[i]:
            ans = "Yes"
            break

    # 答えを返す
    return(ans)

# このプログラムを直接呼び出した場合
# (テストのときに画面からの入力と、画面への出力を行わないようにするための機構)
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を数値として扱う(入力は1～100の範囲に限定されている。)
    n = int(input())
    # 2行目の入力を文字列として扱う
    t = input()
    # 3行目の入力を文字列として扱う
    a = input()
    
    # 処理を呼び出し、結果を出力する
    print(func(n, t, a))

