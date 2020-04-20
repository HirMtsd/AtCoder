# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 163-A'
# 2020/04/20

def abc(R):
    # 円周率の準備
    pi = 3.141592
    
    # 計算
    ans = R * 2 * pi
    
    # 答え
    return(ans)


# バッチスタート
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を数値として扱う
    R = int(input())
    
    # 関数呼び出し
    f = abc(R)
    
    # 答えの出力
    print(f)
