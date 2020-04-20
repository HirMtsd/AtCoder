# coding: utf-8
# Copyright (C) 2020 Matsuda.Hironobu. All Rights Reserved.
# Code for 'AtCoder Beginner Contest 163-A' Test-Code
# 2020/04/20

from unittest import TestCase, main
from abc163a import abc

# TestCaseが呼び出すためのクラス
class TestABC163A(TestCase):
    # テストメソッド
    def test_by_parameters(self):
        # テストパターン
        test_patterns = [
            (1, 6.28318530717958623200),
            (73, 458.67252742410977361942),
            (100, 628.31853071795862320),
        ]
        
        # テストパターンだけ繰り返す
        for p1, expected in test_patterns:
            with self.subTest(p1=p1):
                # 10の-2乗誤差許容らしいので、上5桁くらいで比較
                self.assertEqual(str(abc(p1))[0:5], str(expected)[0:5])

