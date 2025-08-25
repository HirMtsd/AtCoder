# coding: utf-8
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 413-A'
# 2025/08/14

# 実際の処理
def func(n, m, a):
    # 答は"Yes"か"No"なので、最初に"No"を設定
    ans = "No"
    
    # 品物の大きさの総和
    all = 0
    
    # n回ループ処理
    for i in range(n):
        # 数値リストの中身を全部足す
        all += a[i]
    
    # mと比較
    if all <= m:
        ans = "Yes"

    # 答えを返す
    return(ans)

# このプログラムを直接呼び出した場合
# (テストのときに画面からの入力と、画面への出力を行わないようにするための機構)
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を2つの数値として扱う(入力は1～100,1～10000の範囲に限定されている。)
    n,m = map(int, input().split())
    # 2行目の入力をn個の数値リストとして扱う
    a = [int(s) for s in input().split()]
    
    # 処理を呼び出し、結果を出力する
    print(func(n, m, a))

