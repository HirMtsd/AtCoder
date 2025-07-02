# coding: utf-8
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 409-B'
# 2025/07/02

# 実際の処理
def func(n, a):
    # ここにロジックを書く
    # 数列aの値が0～nのどれに当たるか調べるためのワーク
    c = [0]*(n+1)
    
    # n回ループ処理
    for i in range(n):
        # 数列aの値をワークにセット
        # ただし数列aの値がn以上の場合はnにセット
        if a[i] > n:
            c[n] += 1
        else:
            c[a[i]] += 1

    # 要素数の積算個数
    s = 0
    # n～0までループ処理
    for j in range(n, 0, -1):
        # 積算個数に要素の個数を加算
        s += c[j]
        # 積算個数がj以上の場合、jを返す
        if s >= j:
            return(j)
    

    # 最後まで離脱しなかった場合0を返す
    return(0)

# このプログラムを直接呼び出した場合
# (テストのときに画面からの入力と、画面への出力を行わないようにするための機構)
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を数値として扱う(入力は1～100の範囲に限定されている。)
    n = int(input())
    # 2行目の入力をn個の数値リストとして扱う
    a = [int(s) for s in input().split()]
    
    # 処理を呼び出し、結果を出力する
    print(func(n, a))

