# coding: utf-8
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 413-B'
# 2025/08/14

# 実際の処理
def func(n, s):
    # 重複を除く集合の数を数えたいので、連結文字列setを準備する
    cset = set()
    
    # n*n回ループ処理
    for i in range(n):
        for j in range(n):
            # i = jのときスキップ
            if i == j:
                continue
            # SiとSjを結合し、連結文字列setに追加
            cset.add(s[i]+s[j])

    # 連結文字列setの数を返す
    return(len(cset))

# このプログラムを直接呼び出した場合
# (テストのときに画面からの入力と、画面への出力を行わないようにするための機構)
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を数値として扱う(入力は2～100の範囲に限定されている。)
    n = int(input())
    # 2行目以降の入力をn個の文字列リストとして扱う
    s = [""]*n
    for i in range(n):
        s[i] = input()
    
    # 処理を呼び出し、結果を出力する
    print(func(n, s))

