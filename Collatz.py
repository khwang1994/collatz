#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------


CACHE = [0] * 1000000
MAX_VAL = 837799  # value with the largest cycle length in the range
MAX_CL = 525

# ------------
# collatz_read
# ------------


def collatz_read(input_str):
    """
    read two ints
    input arr string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    arr = input_str.split()
    return [int(arr[0]), int(arr[1])]


# ------------
# collatz_eval
# ------------


def collatz_eval(start, end):
    """
    start is the beginning of the range, inclusive
    end is the end       of the range, inclusive
    return the max cycle length of the range [start, end]
    """
    # <your code>

    first = min(start, end)  # first val in the range
    last = max(start, end)  # last val in the range
    curr_cl = 0
    mcl = 0  # stores the max cycle length

    assert first > 0
    assert last < 1000000
    assert first <= last

    #   Max cycle length optimization
    if first <= MAX_VAL <= last:
        return MAX_CL

    #   Upper half of range optimization
    #   Given b, e, m where m = (e/2) + 1 and b < m, mcl(b, e) == mcl(m, e)
    middle = (last >> 1) + 1
    if first < middle:
        first = middle

    #   MAIN LOOP to find max cycle length.
    for num in range(first, last + 1):
        if CACHE[num] != 0:  # If num is already in the lazy cache (CACHE)
            curr_cl = CACHE[num]
        else:
            curr_cl = collatz_cycle_len(num)

        #   Compare cycle len of num to current max cycle len
        if curr_cl > mcl:
            mcl = curr_cl

    return mcl

# ------------
# collatz_cycle_length
# ------------


def collatz_cycle_len(num):
    """
    Returns cycle length of num
    Also stores other cycle lengths it finds into CACHE
    """

    #   As cycle len of num is calculated, tb (traceback) cache will store values along
    #   the way and use the cycle len of num to determine the cycle len of each of
    #   these values
    tb_cache = [num]
    cycle_len = 1

    while num > 1:
        #   Case in which you run into a value already in the eager cache
        if num < len(CACHE) and CACHE[num] != 0:
            cycle_len = cycle_len + CACHE[num] - 1
            num = 1  # to exit the while loop

        #   Even number case
        elif num % 2 == 0:
            num >>= 1   # divide num by 2
            cycle_len += 1
            tb_cache += [num]

        #   Odd number case
        else:
            num = num + (num >> 1) + 1
            cycle_len += 2
            tb_cache += [0, num]

    #   Going back through tb_cache and calculated cycle lengths for
    #   each value based on the cycle len of num
    #   Index is the amount you subtract from the cycle length of the initial input in
    #   order to find the cycle length of the value stored
    for index, item in enumerate(tb_cache):
        if item < len(CACHE) and item != 0 and CACHE[item] == 0:
            CACHE[item] = cycle_len - index

    return cycle_len


# -------------
# collatz_print
# -------------


def collatz_print(result, start, end, mcl):
    """
    print three ints
    result is a writer
    start is the beginning of the range, inclusive
    end is the end       of the range, inclusive
    mcl is the max cycle length
    """
    result.write(str(start) + " " + str(end) + " " + str(mcl) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(input_str, result):
    """
    input_str is a reader
    result is a writer
    """

    for val in input_str:
        if not val.strip():
            break

        start, end = collatz_read(val)
        mcl = collatz_eval(start, end)
        collatz_print(result, start, end, mcl)
