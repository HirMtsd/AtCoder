# -*- coding: utf-8 -*-
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 423-C'
# Date(ISO 8601): 2025-10-01

"""
標準入力から2つの整数n,rと、数値配列lを読み込む
2<=n<=100、0<=r<=n、配列lの要素数はn、li∈{0,1}
nは扉の数、n+1を部屋の数とし、
数値配列lの要素liは、部屋i-1と部屋iの間の扉の状態(0:開,1:閉)
最初に部屋rから移動しはじめて、隣の部屋との間の扉の開閉ができる場合、
全ての扉を閉めるには何回改姓動作が必要かを返す。
"""

# 主処理
def func(n, r, l):
    # 答えのデフォルト値を準備
    ans = 0

    # 配列中に0が0個の場合は何もせずに終了
    # なので、1以上の場合のみ数える
    if l.count(0) >= 1:
        # 自分の位置より前に0の扉がある場合、開閉処理の開始位置はその部屋
        # 自分の位置より前に0の扉がない場合、開閉処理の開始位置は自分の部屋
        lb = l[:r]
        if lb.count(0) > 0:
            s_pos = lb.index(0)
        else:
            s_pos = r
        
        # 自分の位置より後に0の扉がある場合、開閉処理の終了位置はその部屋
        # 自分の位置より後に0の扉がない場合、開閉処理の終了位置は自分の部屋
        lr = l[r:]
        if lr.count(0) > 0:
            l.reverse()
            e_pos = n - l.index(0)
            l.reverse()
        else:
            e_pos = r
        
        #print("s,r,e",s_pos,r_pos,e_pos)
        # 1の扉は開閉動作が2回必要
        # 0の扉は開閉動作が1回必要
        for i in range(s_pos, e_pos):
            if l[i] == 0:
                ans += 1
            else:
                ans += 2
    
    # 答えを返す
    return(ans)

# このプログラムを直接呼び出した場合のみ実行する部分
# (importで別ファイルから呼び出した場合にはこの部分は実行しない)
# テスト時に「標準入力」からの入力と、「標準出力」への出力をしないための機構
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を2つの数値として扱う(入力はぞれぞれ1～10^5の範囲に限定されている。)
    n,r = map(int, input().split())
    # 2行目の入力をn個の数値リストとして扱う
    l = [int(s) for s in input().split()]
    
    # 処理を呼び出し、結果を出力する
    print(func(n, r, l))

