# coding: utf-8
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 413-C'
# 2025/08/14

# 実際の処理
def func(n, q):
    # クエリを保存するlistを用意する。(リストには[c(繰り返し数),x(値)]のリストを格納する。)
    A = []
    # 答のリストを用意しておく
    ans = []

    # クエリをひとつづつ処理していく
    cnt = 0
    for i in q:
        # 1文字目が1の場合
        if i[0] == 1:
            # クエリの値を追加する
            c = i[1]
            x = i[2]
            A.append([c, x])
        # 1文字目が2の場合
        if i[0] == 2:
            # 必要な個数を確認する
            k = i[1]
            # 部分解を初期化
            part = 0
            # ループ処理
            while True:
                # Aの先頭からcとxを取り出す。
                c = A[cnt][0]
                x = A[cnt][1]
                # cがk以上の場合、部分解にx*kを足し、Aの先頭のcの値をc-kに更新する(ループを終了)
                if c >= k:
                    part += x * k
                    A[cnt][0] = c - k
                    break
                # cがkより小さい場合、部分解にx*cを足し、kをk-cに更新し、Aのクエリカウンタを1つ進める(ループ継続)
                if c < k:
                    part += x * c
                    k = k - c
                    cnt += 1
            
            ans.append(part)

    # 答を返す
    return(ans)

# このプログラムを直接呼び出した場合
# (テストのときに画面からの入力と、画面への出力を行わないようにするための機構)
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を数値として扱う(入力は2～2*10^5の範囲に限定されている。)
    n = int(input())
    # 2行目以降の入力をn個の数値リストとして扱う
    q = [""]*n
    for i in range(n):
        q[i] = [int(s) for s in input().split()]
    
    # 処理を呼び出し、結果を出力する
    ans = func(n, q)
    print(*ans, sep='\n')

