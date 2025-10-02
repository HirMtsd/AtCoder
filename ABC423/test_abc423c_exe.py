# -*- coding: utf-8 -*-
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 423-C Test'
# Date(ISO 8601): 2025-10-01

"""
「コマンドラインからプログラムを呼びだす形式」で実行するためのテストプログラム
例1：
python (this_file) python (test_target_file).py
例2：
python (this_file) java (test_target_file).java
"""

# unittestの準備
import os
import sys
import unittest
import time

# サブプロセス実行
import subprocess

# 実行時のディレクトリからも対象ファイルを検索可能にしておく
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

# テストメソッド
def test_func(args_str):
    # テストデータの準備
    # テストデータは1行1件。
    # 最初の引数はテスト番号(なんでもよい)。最後の引数は期待値
    # データはn(部屋の数)r(最初にいる部屋)l(部屋間のドアの状態を示す数値リスト0=開,1=閉)
    # 2<=n<=2*10^5,0<=r<=n,lの要素数はn,li∈{0,1}
    l200000 = [1]*2*10**5
    l200000[0] = 0
    l200000[2*10**5-1] = 0
    test_patterns = [
        # 課題に記載のケース
        ( 1,     6,     3, [1, 0, 0, 1, 0, 0]      ,   6),
        ( 2,     2,     1, [0, 0]                  ,   2),
        ( 3,     8,     2, [0, 1, 0, 0, 1, 0, 1, 1],   8),
        # n=2のケース
        (11,     2,     0, [0, 0]     ,   2),
        (12,     2,     1, [0, 0]     ,   2), # ケース2と同じ
        (13,     2,     2, [0, 0]     ,   2),
        (14,     2,     0, [0, 1]     ,   1),
        (15,     2,     1, [0, 1]     ,   1),
        (16,     2,     2, [0, 1]     ,   3),
        (17,     2,     0, [1, 0]     ,   3),
        (18,     2,     1, [1, 0]     ,   1),
        (19,     2,     2, [1, 0]     ,   1),
        (20,     2,     0, [1, 1]     ,   0), # 既に全部閉まっている
        (21,     2,     1, [1, 1]     ,   0), # 既に全部閉まっている
        (22,     2,     2, [1, 1]     ,   0), # 既に全部閉まっている
        # n=3のケース
        (31,     3,     0, [0, 0, 0]  ,   3),
        (32,     3,     1, [0, 0, 0]  ,   3),
        (33,     3,     2, [0, 0, 0]  ,   3),
        (34,     3,     3, [0, 0, 0]  ,   3),
        (35,     3,     0, [0, 0, 1]  ,   2),
        (36,     3,     1, [0, 0, 1]  ,   2),
        (37,     3,     2, [0, 0, 1]  ,   2),
        (38,     3,     3, [0, 0, 1]  ,   4),
        (39,     3,     0, [0, 1, 0]  ,   4),
        (40,     3,     1, [0, 1, 0]  ,   4),
        (41,     3,     2, [0, 1, 0]  ,   4),
        (42,     3,     3, [0, 1, 0]  ,   4),
        (43,     3,     0, [0, 1, 1]  ,   1),
        (44,     3,     1, [0, 1, 1]  ,   1),
        (45,     3,     2, [0, 1, 1]  ,   3),
        (46,     3,     3, [0, 1, 1]  ,   5),
        (47,     3,     0, [1, 0, 0]  ,   4),
        (48,     3,     1, [1, 0, 0]  ,   2),
        (49,     3,     2, [1, 0, 0]  ,   2),
        (50,     3,     3, [1, 0, 0]  ,   2),
        (51,     3,     0, [1, 0, 1]  ,   3),
        (52,     3,     1, [1, 0, 1]  ,   1),
        (53,     3,     2, [1, 0, 1]  ,   1),
        (54,     3,     3, [1, 0, 1]  ,   3),
        (55,     3,     0, [1, 1, 0]  ,   5),
        (56,     3,     1, [1, 1, 0]  ,   3),
        (57,     3,     2, [1, 1, 0]  ,   1),
        (58,     3,     3, [1, 1, 0]  ,   1),
        (59,     3,     0, [1, 1, 1]  ,   0), # 既に全部閉まっている
        (60,     3,     1, [1, 1, 1]  ,   0), # 既に全部閉まっている
        (61,     3,     2, [1, 1, 1]  ,   0), # 既に全部閉まっている
        (62,     3,     3, [1, 1, 1]  ,   0), # 既に全部閉まっている
        # n=100のケース
        (71, 2*10**5,   0, [0]*2*10**5,   2*10**5),
        (72, 2*10**5,  10, l200000    ,   399998),
    ]

    # データ分だけテストの実行
    for no, param1, param2, param3, expected in test_patterns:
        # 開始時刻取得
        t_s = time.time()
        # テストデータの一時ファイルへの出力
        with open("abc423c_test_data.txt", "w") as of:
            print(str(param1) + " " + str(param2), file=of)
            print(' '.join(map(str, param3)), file=of)
        # テスト実行
        result = subprocess.check_output("type abc423c_test_data.txt | " + args_str, shell=True)
        # 期待値(expected)と結果の比較
        if result.decode().rstrip() != str(expected):
            print("ERROR", no, "result=[" + result.decode().rstrip() + "]", expected)
        else:
            print("OK", no)
        # 終了時刻取得
        t_e = time.time()
        print("exec_time", no, t_e - t_s)

# このプログラムを直接呼び出した場合のみ実行する部分
# (importで別ファイルから呼び出した場合にはこの部分は実行しない)
if __name__ == "__main__":
    # コマンドライン引数の取得
    args = sys.argv

    # 実行時引数の数チェック
    if len(args) != 3:
        print("Usage: python (this_file) python (test_target_file).py")
        print("       or")
        print("       python (this_file) java (test_target_file).java")
        exit()

    # 引数を文字列に組み立て(第一引数はこのファイルなので、第2引数+" "+第3引数)
    arg_str = ""
    for i in range(1, len(args)):
        arg_str += args[i] + " "
    print(arg_str)

    test_func(arg_str)

