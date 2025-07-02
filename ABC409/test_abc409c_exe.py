# coding: utf-8
# Copyright (C) 2025 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 409-C Test'
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
    # データはn(点の数)l(円周)d[](点間の距離)
    test_patterns = [
        # 課題に記載のケース
        ( 1,  5,  6, [4, 3, 1, 2,], 2),
        ( 2,  4,  4, [1, 1, 1,], 0),
        ( 3, 10, 12, [4, 4, 5, 7, 1, 7, 0, 8, 5,], 13),
        # L=3のケース
        ( 4,  3,  3, [0, 0,], 0),
        ( 5,  3,  3, [0, 1,], 0),
        ( 6,  3,  3, [1, 1,], 1),
        ( 7,  6,  3, [1, 1, 1, 1, 1], 8),
        ( 8,  9,  3, [1, 1, 1, 1, 1, 1, 1, 1], 27),
        ( 9,  3*10**5,  3, [1]*3*10**5, 10**15),
        # L=4のケース
        (10,  4,  3*10**5, [1]*3*10**5, 0),
        # L=5のケース
        (11,  5,  3*10**5, [1]*3*10**5, 0),
        # L=3*10**5のケース
        (12, 3*10**5, 3*10**5, [1]*3*10**5, 10**5),
    ]

    # データ分だけテストの実行
    for no, param1, param2, param3, expected in test_patterns:
        # 開始時刻取得
        t_s = time.time()
        # テストデータの一時ファイルへの出力
        with open("abc409c_test_data.txt", "w") as of:
            print(str(param1) + " " + str(param2), file=of)
            print(' '.join(map(str, param3)), file=of)
        # テスト実行
        result = subprocess.check_output("type abc409c_test_data.txt | " + args_str, shell=True)
        # 期待値(expected)と結果の比較
        if result.decode().rstrip() != str(expected):
            print("ERROR", no, "[" + result.decode().rstrip() + "]", "[" + str(expected) + "]")
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

