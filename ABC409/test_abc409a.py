# coding: utf-8
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 409-A Test'
# 2025/07/02

# unittestの準備
import os
import sys
import unittest

# 実行時のディレクトリからも対象ファイルを検索可能にしておく
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

# テスト対象の「ファイル名」と「関数名」を指定
from abc409a import func

# TestCaseが呼び出すためのクラス
class TestAbc409a(unittest.TestCase):
    # テストメソッド
    def test_func(self):
        # テストデータの準備
        # テストデータは1行1件。
        # データはn(文字列の長さ)t(文字列：高橋君の要望ox)a(文字列：青木君の要望ox)
        # 最後の引数は期待値
        test_patterns = [
        # 課題に記載のケース
            (  4, "oxoo", "xoox", "Yes"),
            (  5, "xxxxx", "ooooo", "No"),
            ( 10, "xoooxoxxxo", "ooxooooxoo", "Yes"),
            # N=1のケース
            (  1, "x", "x", "No"),
            (  1, "x", "o", "No"),
            (  1, "o", "x", "No"),
            (  1, "o", "o", "Yes"),
            # N=2のケース
            (  2, "xx", "xx", "No"),
            (  2, "xx", "xo", "No"),
            (  2, "xx", "ox", "No"),
            (  2, "xx", "oo", "No"),
            (  2, "xo", "xx", "No"),
            (  2, "xo", "ox", "No"),
            (  2, "ox", "xx", "No"),
            (  2, "ox", "xo", "No"),
            (  2, "oo", "xx", "No"),
            (  2, "xo", "xo", "Yes"),
            (  2, "xo", "oo", "Yes"),
            (  2, "ox", "ox", "Yes"),
            (  2, "ox", "oo", "Yes"),
            (  2, "oo", "ox", "Yes"),
            (  2, "oo", "xo", "Yes"),
            (  2, "oo", "oo", "Yes"),
            # N=100の最悪ケース
            (100, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "No"),
            (100, "oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "Yes"),
            (100, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo", "Yes"),
        ]

        # データ分だけテストの実行
        for param1, param2, param3, expected in test_patterns:
            with self.subTest(param1=param1, param2=param2, param3=param3):
                # 期待値(expected)と結果の比較
                self.assertEqual(func(param1, param2, param3), expected)

if __name__ == "__main__":
    unittest.main()

