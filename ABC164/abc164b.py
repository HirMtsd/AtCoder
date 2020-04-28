# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 164-B'
# 2020/04/26

def abc(A, B, C, D):
    # 答えの準備
    ans = 'No'
    
    # 比較
    while True:
        C -= B
        if C <= 0:
            ans = 'Yes'
            break
        A -= D
        if A <= 0:
            break
    
    # 答え
    return(ans)


# バッチスタート
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を空白で分割された4つの数値として扱う
    A, B, C, D = map(int, input().split())
    
    # 関数呼び出し
    f = abc(A, B, C, D)
    
    # 答えの出力
    print(f)
