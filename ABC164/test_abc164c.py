# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 164-C' Test-Code
# 2020/04/26

from unittest import TestCase, main
from abc164c import abc

# TestCaseが呼び出すためのクラス
class TestABC164C(TestCase):
    # テストメソッド
    def test_by_parameters(self):
        # テスト用配列
        l1 = ['abcdefghij'] * 200000
        
        # テストパターン
        test_patterns = [
            (3, ['apple', 'orange', 'apple'], 2),
            (5, ['grape', 'grape', 'grape', 'grape', 'grape'], 1),
            (4, ['aaaa', 'a', 'aaa', 'aa'], 4),
            (1, ['a'], 1),
            (200000, l1, 1),
        ]
        
        # テストパターンだけ繰り返す
        for p1, p2, expected in test_patterns:
            with self.subTest(p1=p1, p2=p2):
                # 比較
                self.assertEqual(abc(p1, p2), expected)

