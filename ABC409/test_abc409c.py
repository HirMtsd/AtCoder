# coding: utf-8
# Copyright (C) 2025 HirMtsd. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 409-C Test'
# 2025/07/02

# unittestの準備
import os
import sys
import unittest

# 実行時のディレクトリからも対象ファイルを検索可能にしておく
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

# テスト対象の「ファイル名」と「関数名」を指定
from abc409c import func

# TestCaseが呼び出すためのクラス
class TestAbc409c(unittest.TestCase):
    # テストメソッド
    def test_func(self):
        # テストデータの準備
        # テストデータは1行1件。
        # データはn(点の数)l(円周)d[](点間の距離)
        # 最後の引数は期待値
        test_patterns = [
            # 課題に記載のケース
            (  5,  6, [4, 3, 1, 2,], 2),
            (  4,  4, [1, 1, 1,], 0),
            ( 10, 12, [4, 4, 5, 7, 1, 7, 0, 8, 5,], 13),
            # L=3のケース
            (  3,  3, [0, 0,], 0),
            (  3,  3, [0, 1,], 0),
            (  3,  3, [1, 1,], 1),
            (  6,  3, [1, 1, 1, 1, 1], 8),
            (  9,  3, [1, 1, 1, 1, 1, 1, 1, 1], 27),
            (  3*10**5,  3, [1]*3*10**5, 10**15),
            # L=4のケース
            (  3,  4, [1, 1, 1], 0),
            (  3*10**5, 4, [1]*3*10**5, 0),
            # L=5のケース
            (  3,  5, [1, 1, 1], 0),
            (  3*10**5, 5, [1]*3*10**5, 0),
            # L=3*10**5のケース
            ( 3*10**5, 3*10**5, [1]*3*10**5, 10**5),
        ]

        # データ分だけテストの実行
        for param1, param2, param3, expected in test_patterns:
            with self.subTest(param1=param1, param2=param2, param3=param3):
                # 期待値(expected)と結果の比較
                self.assertEqual(func(param1, param2, param3), expected)

if __name__ == "__main__":
    unittest.main()

