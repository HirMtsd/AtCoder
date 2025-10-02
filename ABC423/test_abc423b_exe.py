# -*- coding: utf-8 -*-
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 423-B Test'
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
    # データはn(部屋の数)l(部屋間のドアの状態を示す数値リスト0=開,1=閉)
    # 2<=n<=100,lの要素数はn,li∈{0,1}
    test_patterns = [
        # 課題に記載のケース
        ( 1,   5, [0, 1, 0, 0, 1],   3),
        ( 2,   3, [1, 0, 1]      ,   2),
        ( 3,   8, [0, 0, 1, 1, 0, 1, 0, 0],   3),
        # n=2のケース
        (11,   2, [0, 0]     ,   0),
        (12,   2, [0, 1]     ,   0),
        (13,   2, [1, 0]     ,   0),
        (14,   2, [1, 1]     ,   1),
        # n=3のケース
        (21,   3, [0, 0, 0]  ,   0),
        (22,   3, [0, 0, 1]  ,   0),
        (23,   3, [0, 1, 0]  ,   0),
        (24,   3, [0, 1, 1]  ,   1),
        (25,   3, [1, 0, 0]  ,   0),
        (26,   3, [1, 0, 1]  ,   2), # ケース2と同じ
        (27,   3, [1, 1, 0]  ,   1),
        (28,   3, [1, 1, 1]  ,   2),
        # n=100のケース
        (31, 100, [0]*100,   0),
        (32, 100, [1]*100,  99),
    ]

    # データ分だけテストの実行
    for no, param1, param2, expected in test_patterns:
        # 開始時刻取得
        t_s = time.time()
        # テストデータの一時ファイルへの出力
        with open("abc423b_test_data.txt", "w") as of:
            print(str(param1), file=of)
            print(' '.join(map(str, param2)), file=of)
        # テスト実行
        result = subprocess.check_output("type abc423b_test_data.txt | " + args_str, shell=True)
        # 期待値(expected)と結果の比較
        if int(result.decode().rstrip()) != expected:
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

