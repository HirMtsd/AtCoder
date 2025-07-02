# coding: utf-8
# Copyright (C) 2025 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 409-A Test'
# 2025/07/02

# どのような実行形式ファイルでもテストするためのテストプログラム

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
    # データはn(文字列の長さ)t(文字列：高橋君の要望ox)a(文字列：青木君の要望ox)
    test_patterns = [
        # 課題に記載のケース
        ( 1,  4, "oxoo", "xoox", "Yes"),
        ( 2,  5, "xxxxx", "ooooo", "No"),
        ( 3, 10, "xoooxoxxxo", "ooxooooxoo", "Yes"),
        # N=1のケース
        ( 4,  1, "x", "x", "No"),
        ( 5,  1, "x", "o", "No"),
        ( 6,  1, "o", "x", "No"),
        ( 7,  1, "o", "o", "Yes"),
        # N=2のケース
        (11,  2, "xx", "xx", "No"),
        (12,  2, "xx", "xo", "No"),
        (13,  2, "xx", "ox", "No"),
        (14,  2, "xx", "oo", "No"),
        (15,  2, "xo", "xx", "No"),
        (16,  2, "xo", "ox", "No"),
        (17,  2, "ox", "xx", "No"),
        (18,  2, "ox", "xo", "No"),
        (19,  2, "oo", "xx", "No"),
        (20,  2, "xo", "xo", "Yes"),
        (21,  2, "xo", "oo", "Yes"),
        (22,  2, "ox", "ox", "Yes"),
        (23,  2, "ox", "oo", "Yes"),
        (24,  2, "oo", "ox", "Yes"),
        (25,  2, "oo", "xo", "Yes"),
        (26,  2, "oo", "oo", "Yes"),
        # N=100の最悪ケース
        (31,100, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "No"),
        (32,100, "oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "Yes"),
        (33,100, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo", "Yes"),
    ]

    # データ分だけテストの実行
    for no, param1, param2, param3, expected in test_patterns:
        # 開始時刻取得
        t_s = time.time()
        # テストデータの一時ファイルへの出力
        with open("abc409a_test_data.txt", "w") as of:
            print(param1, file=of)
            print(param2, file=of)
            print(param3, file=of)
        # テスト実行
        result = subprocess.check_output("type abc409a_test_data.txt | " + args_str, shell=True)
        # 期待値(expected)と結果の比較
        if result.decode().rstrip() != expected:
            print("ERROR", no, "result=[" + result.decode().rstrip() + "]", expected)
        else:
            print("OK", no)
        # 終了時刻取得
        t_e = time.time()
        print("exec_time", no, t_e - t_s)

if __name__ == "__main__":
    # コマンドライン引数の取得
    args = sys.argv

    if args == 1:
        print("引数にテストを実行するプログラムを指定してください")

    # 引数を文字列に組み立て
    arg_str = ""
    for i in range(1, len(args)):
        arg_str += args[i] + " "
    print(arg_str)

    test_func(arg_str)

