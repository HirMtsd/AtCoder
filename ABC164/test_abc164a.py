# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 164-A' Test-Code
# 2020/04/27

from unittest import TestCase, main
from abc164a import abc

# TestCaseが呼び出すためのクラス
class TestABC164A(TestCase):
    # テストメソッド
    def test_by_parameters(self):
        # テストパターン
        test_patterns = [
            (4, 5, 'unsafe'),
            (100, 2, 'safe'),
            (10, 10, 'unsafe'),
            (1, 1, 'unsafe'),
            (1, 100, 'unsafe'),
            (100, 1, 'safe'),
            (100, 100, 'unsafe'),
        ]
        
        # テストパターンだけ繰り返す
        for p1, p2, expected in test_patterns:
            with self.subTest(p1=p1, p2=p2):
                # 比較
                self.assertEqual(abc(p1, p2), expected)

