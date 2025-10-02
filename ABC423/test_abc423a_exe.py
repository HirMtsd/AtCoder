# -*- coding: utf-8 -*-
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 423-A Test'
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
    # データはx(残高)c(手数料) 
    # 1<=x<=10^7,1<=c<=999
    test_patterns = [
        # 課題に記載のケース
        ( 1,   650000,    8, 644000),
        ( 2,     1003,    4, 0),
        ( 3, 10000000,   24, 9765000),
        # x=1のケース
        (11,        1,    1, 0),
        (12,        1,  999, 0),
        # x=999のケース
        (21,      999,    1, 0),
        (22,      999,  999, 0),
        # x=1000のケース
        (31,     1000,    1, 0),
        (32,     1000,  999, 0),
        # x=1001のケース
        (41,     1001,    1, 1000),
        (42,     1001,    2, 0),
        (43,     1001,  999, 0),
        # x=1002のケース
        (51,     1002,    1, 1000),
        (52,     1002,    2, 1000),
        (53,     1002,    3, 0),
        (54,     1002,  999, 0),
        # x=99999990のケース
        (61,  9999999,    1,  9990000),
        (62,  9999999,    2,  9980000),
        (63,  9999999,    3,  9970000),
        (64,  9999999,  999,  5002000),
        # x=10000000のケース
        (71, 10000000,    1,  9990000),
        (72, 10000000,    2,  9980000),
        (73, 10000000,    3,  9970000),
        (74, 10000000,  999,  5002000),
    ]

    # データ分だけテストの実行
    for no, param1, param2, expected in test_patterns:
        # 開始時刻取得
        t_s = time.time()
        # テスト実行
        result = subprocess.check_output("echo " + str(param1) + " " + str(param2) + " | " + args_str, shell=True)
        # 期待値(expected)と結果の比較
        if result.decode().rstrip() != str(expected):
            print("ERROR", no, "result=[" + result.decode().rstrip() + "]", str(expected))
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

