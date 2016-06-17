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

    def test_read_1(self):
        input_str = "1 10\n"
        start, end = collatz_read(input_str)
        self.assertEqual(start,  1)
        self.assertEqual(end, 10)

    def test_read_2(self):
        input_str = "15 15\n"
        start, end = collatz_read(input_str)
        self.assertEqual(start,  15)
        self.assertEqual(end, 15)

    def test_read_3(self):
        input_str = "2 500\n"
        start, end = collatz_read(input_str)
        self.assertEqual(start,  2)
        self.assertEqual(end, 500)

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

    def test_eval_6(self):
        result = collatz_eval(1, 999999)
        self.assertEqual(result, 525)

    def test_eval_7(self):
        result = collatz_eval(999999, 999999)
        self.assertEqual(result, 259)

    # -----
    # print
    # -----

    def test_print_1(self):
        result = StringIO()
        collatz_print(result, 1, 10, 20)
        self.assertEqual(result.getvalue(), "1 10 20\n")

    def test_print_2(self):
        result = StringIO()
        collatz_print(result, 100, 200, 125)
        self.assertEqual(result.getvalue(), "100 200 125\n")

    def test_print_3(self):
        result = StringIO()
        collatz_print(result, 201, 210, 89)
        self.assertEqual(result.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        input_str = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        result = StringIO()
        collatz_solve(input_str, result)
        self.assertEqual(
            result.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        input_str = StringIO("1 1\n2 2\n3 3\n4 4\n")
        result = StringIO()
        collatz_solve(input_str, result)
        self.assertEqual(
            result.getvalue(), "1 1 1\n2 2 2\n3 3 8\n4 4 3\n")

    def test_solve_3(self):
        input_str = StringIO(
            "3 4545\n9987 77833\n837799 837799\n38949 39734\n")
        result = StringIO()
        collatz_solve(input_str, result)
        self.assertEqual(
            result.getvalue(), "3 4545 238\n9987 77833 351\n837799 837799 525\n38949 39734 275\n")

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
Ran 16 tests in 0.357s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          53      1     24      1    97%   147, 146->147
TestCollatz.py      69      0      0      0   100%
------------------------------------------------------------
TOTAL              122      1     24      1    99%
"""
