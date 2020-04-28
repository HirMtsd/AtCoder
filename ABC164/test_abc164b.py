# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 164B' Test-Code
# 2020/04/27

from unittest import TestCase, main
from abc164b import abc

# TestCaseが呼び出すためのクラス
class TestABC164B(TestCase):
    # テストメソッド
    def test_by_parameters(self):
        # テスト用配列
        l1 = '1' * 200000
        
        # テストパターン
        test_patterns = [
            (10, 9, 10, 10, 'No'),
            (46, 4, 40, 5, 'Yes'),
            (1, 1, 1, 1, 'Yes'),
            (100, 100, 100, 100, 'Yes'),
        ]
        
        # テストパターンだけ繰り返す
        for p1, p2, p3, p4, expected in test_patterns:
            with self.subTest(p1=p1, p2=p2, p3=p3, p4=p4):
                # 比較
                self.assertEqual(abc(p1, p2, p3, p4), expected)

