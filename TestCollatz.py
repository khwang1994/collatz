#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        input_str = "1 10\n"
        start, end = collatz_read(input_str)
        self.assertEqual(start,  1)
        self.assertEqual(end, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        result = collatz_eval(1, 10)
        self.assertEqual(result, 20)

    def test_eval_2(self):
        result = collatz_eval(100, 200)
        self.assertEqual(result, 125)

    def test_eval_3(self):
        result = collatz_eval(201, 210)
        self.assertEqual(result, 89)

    def test_eval_4(self):
        result = collatz_eval(900, 1000)
        self.assertEqual(result, 174)

    def test_eval_5(self):
        result = collatz_eval(1, 1)
        self.assertEqual(result, 1)

    
    # -----
    # print
    # -----

    def test_print(self):
        result = StringIO()
        collatz_print(result, 1, 10, 20)
        self.assertEqual(result.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        input_str = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        result = StringIO()
        collatz_solve(input_str, result)
        self.assertEqual(
            result.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
