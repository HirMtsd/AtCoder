# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 163-C' Test-Code
# 2020/04/21

from unittest import TestCase, main
from abc163c import abc

# TestCaseが呼び出すためのクラス
class TestABC163C(TestCase):
    # テストメソッド
    def test_by_parameters(self):
        # テスト用配列
        l1_199999 = [1] * 199999
        la = [0] * 200000
        la[0] = 199999
        # テストパターン
        test_patterns = [
            (5, [1, 1, 2, 2], [2, 2, 0, 0, 0]),
            (10, [1, 1, 1, 1, 1, 1, 1, 1, 1], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            (7, [1, 2, 3, 4, 5, 6], [1, 1, 1, 1, 1, 1, 0]),
            (2, [1], [1, 0]),
            (200000, l1_199999, la),
        ]
        
        # テストパターンだけ繰り返す
        for p1, p2, expected in test_patterns:
            with self.subTest(p1=p1, p2=p2):
                # 比較
                self.assertEqual(abc(p1, p2), expected)

