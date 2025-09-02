# coding: utf-8
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 421-C'
# 2025/09/02

# 実際の処理
def func(n, s):
    # 文字列sの最初の1文字を確認する。
    f = s[0]
    
    # 1文字目がAなら調査対象文字tを"A",1文字目がBならtを"B"とする。
    t = f
    
    # 最終形はtがすべて偶数の位置にあればいい。
    # tの位置を調べて、intの配列に確保する。
    cnt = 0
    tmp = [0]*n
    for i in range(n*2):
        if s[i] == t:
            tmp[cnt] = i
            cnt += 1
    
    # tmp[]のそれぞれの値が本来あるべき位置からどれくらい離れているか確認し、
    # 答えに足していく
    ansa = 0
    for i in range(n):
        # i個目がi*2より大きい場合
        if tmp[i] > i*2:
           ansa += tmp[i] - i*2
        # i個目がi*2より小さい場合
        if tmp[i] < i*2:
           ansa += i*2 - tmp[i]
    
    # tmp[]のそれぞれの値が本来あるべき位置からどれくらい離れているか確認し、
    # 答えに足していく
    ansb = 0
    for i in range(n):
        # i個目がi*2 + 1より大きい場合
        if tmp[i] > i*2 + 1:
           ansb += tmp[i] - (i*2 + 1)
        # i個目がi*2 + 1より小さい場合
        if tmp[i] < i*2 + 1:
           ansb += (i*2 + 1) - tmp[i]
    
    # 答えを返す
    return(min(ansa, ansb))

# このプログラムを直接呼び出した場合
# (テストのときに画面からの入力と、画面への出力を行わないようにするための機構)
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を1つの数値として扱う(入力は1～100に限定されている。)
    n = int(input())
    # 2行目の入力を文字列として扱う(文字列長はn*2に固定されている。)
    s = input()
    
    # 処理を呼び出し、結果を出力する
    print(func(n, s))

