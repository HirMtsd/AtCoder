# coding: utf-8
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 409-C'
# 2025/07/02

# 実際の処理
def func(n, l, d):
    # ここにロジックを書く
    # 円周上の3点が正三角形であるためには、円周が3の倍数でないと不成立
    # なので、まずlが3の倍数でない場合は除外する。
    # print("l,n", l,n)
    if l % 3 != 0:
        return(0)

    # 円周上の点の位置に点があるか調べるワーク
    w = [0]*(l)
    # 頂点には必ず1つ点がある
    w[0] = 1
    # diは円周の始点からのそれぞれの距離を示すので、
    # 積算してlで割ったあまりが位置を示す
    # 積算用ワーク
    s = 0
    # lが3の倍数のとき、始点0からl-1までのどこに点が配置されているか調べる
    # n-1回ループ処理
    for i in range(n-1):
        s += d[i]
        w[s % l] += 1
    
    # for debug
    #print(d)
    #print(w)

    # 答えの準備
    ans = 0
    
    # 始点0からl/3までの距離についてそこから等距離の点を数える。
    # 0からl/3までループ処理
    for j in range(int(l/3)):
        # for debug
        #print("l/3", int(l/3), int(l*2/3))
        #print("j",j,w[j],"j2",j+int(l/3),w[j+int(l/3)],"j3",j+int(l*2/3),w[j+int(l*2/3)])
        ans += w[j] * w[j+int(l/3)] * w[j+int(l*2/3)]

    # 答を返す
    return(ans)

# このプログラムを直接呼び出した場合
# (テストのときに画面からの入力と、画面への出力を行わないようにするための機構)
if __name__ == "__main__":
    # 標準入力処理
    # 1行目の入力を2つの数値として扱う(入力は3～3*10^5の範囲に限定されている。)
    n,l = map(int, input().split())
    # 2行目の入力をl個の数値リストとして扱う
    d = [int(s) for s in input().split()]
    
    # 処理を呼び出し、結果を出力する
    print(func(n, l, d))

