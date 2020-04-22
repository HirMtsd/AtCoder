# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 163-D'
# 2020/04/21

def abc(N, K):
    # 答えの準備
    ans = 0
    
    # 足す個数(K個足す最大値-最小値～N+1個足す最大値-最小値)
    for i in range(K, N+2):
        # i個足すときの最大値は、項数i,初項N-i+1,末項Nの階差数列の和
        max = int(0.5*i*(N-i+1+N))
        # i個足すときの最小値は、項数i,初項0,末項i-1の階差数列の和
        min = int(0.5*i*(0+i-1))
        # 最大値から最小値を引いて、個数なので最初の分1足す
        ans += max - min + 1
    
    # 答え(大きな数字は余りを求める)
    if ans > 10**9 + 7:
        ans = ans % (10**9 + 7)
    return(ans)


# バッチスタート
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を空白で分割された2つの数値として扱う
    N, K = map(int, input().split())
    
    # 関数呼び出し
    f = abc(N, K)
    
    # 答えの出力
    print(f)
