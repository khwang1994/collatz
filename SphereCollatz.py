#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

import sys

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    
    first = min(i, j) #   first val in the range
    last = max(i, j) #    last val in the range
    mcl = 0     #   stores the max cycle length

    assert first > 0 
    assert last < 1000000
    assert first <= last 

    for num in range(first, last + 1):
        curr_cl = 1
        # print("CURRENT NUM:", num)
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                curr_cl += 1
            else:
                num = num + (num >> 1) + 1
                curr_cl += 2
            # print("     ", num, "   cycle len:", curr_cl)

        if curr_cl > mcl:
            mcl = curr_cl

    return mcl

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        if not s.strip():
            break

        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
        
        
collatz_solve(sys.stdin, sys.stdout)