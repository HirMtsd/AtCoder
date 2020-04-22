# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 163-D' Test-Code
# 2020/04/21

from unittest import TestCase, main
from abc163d import abc

# TestCaseが呼び出すためのクラス
class TestABC163D(TestCase):
    # テストメソッド
    def test_by_parameters(self):
        # テストパターン
        test_patterns = [
            (3, 2, 10),
            (200000, 200001, 1),
            (141421, 35623, 220280457),
            (1, 1, 3),
            (1, 2, 1),
            (2, 1, 7),
            (2, 2, 4),
            (200000, 1, 324266530),
            (200000, 2, 324066529),
        ]
        
        # テストパターンだけ繰り返す
        for p1, p2, expected in test_patterns:
            with self.subTest(p1=p1, p2=p2):
                # 比較
                self.assertEqual(abc(p1, p2), expected)

