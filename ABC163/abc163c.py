# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 163-C'
# 2020/04/21

def abc(N, A):
    # 答えの準備
    ans = [0] * N
    
    # 繰返し足し算
    for i in range(0, N - 1):
        ans[A[i] - 1] += 1
    
    # 答え
    return(ans)


# バッチスタート
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を数値として扱う
    N = int(input())
    
    # 2行目の入力を数値のリストとして扱う
    A = list(map(int, input().split()))
    
    # 関数呼び出し
    f = abc(N, A)
    
    # 答えの出力
    for fi in f:
        print(fi)
