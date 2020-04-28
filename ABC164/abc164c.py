# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 164-C'
# 2020/04/26

def abc(N, S):
    # 答えの準備
    ans = 0
    
    # 集合
    str_set = set(S)
    
    # 答え
    ans = len(str_set)
    return(ans)


# バッチスタート
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を数値として扱う
    N = int(input())
    
    # N回入力
    S = []
    for i in range(0, N):
        s = input()
        S.append(s)
    
    # 関数呼び出し
    f = abc(N, S)
    
    # 答えの出力
    print(f)
