# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 163-B'
# 2020/04/21

def abc(N, M, A):
    # 答えの準備
    ans = N
    
    # 繰返し引き算
    for i in range(0, M):
        ans -= A[i]
    
    # 負数の処理
    if ans < 0:
        ans = -1
    
    # 答え
    return(ans)


# バッチスタート
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を空白で分割された2つの数値として扱う
    N, M = map(int, input().split())
    
    # 2行目の入力を数値のリストとして扱う
    A = list(map(int, input().split()))
    
    # 関数呼び出し
    f = abc(N, M, A)
    
    # 答えの出力
    print(f)
