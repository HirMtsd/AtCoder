# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 164-A'
# 2020/04/26

def abc(S, W):
    # 答えの準備
    ans = 'unsafe'
    
    # 比較
    if W < S:
        ans = 'safe'
    
    # 答え
    return(ans)


# バッチスタート
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を空白で分割された2つの数値として扱う
    S, W = map(int, input().split())
    
    # 関数呼び出し
    f = abc(S, W)
    
    # 答えの出力
    print(f)
