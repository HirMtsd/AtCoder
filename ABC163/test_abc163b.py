# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 163-B' Test-Code
# 2020/04/21

from unittest import TestCase, main
from abc163b import abc

# TestCaseが呼び出すためのクラス
class TestABC163B(TestCase):
    # テストメソッド
    def test_by_parameters(self):
        # テスト用配列
        l1_10000 = [1] * 10000
        l99_10000 = [99] * 10000
        
        # テストパターン
        test_patterns = [
            (41, 2, [5, 6], 30),
            (10, 2, [5, 6], -1),
            (11, 2, [5, 6], 0),
            (314, 15, [9, 26, 5, 35, 8, 9, 79, 3, 23, 8, 46, 2, 6, 43, 3], 9),
            (1, 1, [1], 0),
            (1, 1, [2], -1),
            (1, 1, [10000], -1),
            (1, 2, [1, 1], -1),
            (1000000, 10000, l1_10000, 990000),
            (1000000, 10000, l99_10000, 10000),
        ]
        
        # テストパターンだけ繰り返す
        for p1, p2, p3, expected in test_patterns:
            with self.subTest(p1=p1, p2=p2, p3=p3):
                # 比較
                self.assertEqual(abc(p1, p2, p3), expected)

