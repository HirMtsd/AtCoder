# coding: utf-8
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 421-B'
# 2025/09/01

# 題意のrev関数
def rev(x):
    # xを文字列に変換
    xs = str(x)
    
    # xsを反転
    xsr = xs[::-1]
    
    # 反転文字列を数値に変換
    xr = int(xsr)
    
    # 答えを返す
    return(xr)

# 実際の処理
def func(x, y):
    # 正整数列の準備
    ans = [0]*10
    
    # 順に足していく
    ans[0]=x
    ans[1]=y
    for i in range(2, 10, 1):
        ans[i] += rev(ans[i-1] + ans[i-2])
    
    # 答えを返す
    return(ans[9])

# このプログラムを直接呼び出した場合
# (テストのときに画面からの入力と、画面への出力を行わないようにするための機構)
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を2つの数値として扱う(入力はぞれぞれ1～10^5の範囲に限定されている。)
    x,y = map(int, input().split())
    
    # 処理を呼び出し、結果を出力する
    print(func(x, y))

