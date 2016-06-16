#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

lazy_cache = [0] * 1000001
lazy_cache[1] = 1

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

    """
    first = min(start, end) #   first val in the range
    last = max(start, end) #    last val in the range
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

    """

    """
    #   eager cache intialization
    for num in range(1, 1000000):
        index = num #   save the initial num as index into cache
        cyc_len = 1

        cache[2 ** num] = num + 1

        while num is not 1:
            #   case 1: run into value already in cache
            num = int(num)
            if num < 1000000:
                x = cache[num]
                if x != 0:
                    cyc_len = (cyc_len + x) - 1
                    num = 1

            #   case 2: even num
            else:
                if num % 2 == 0:
                    num /= 2
                    cyc_len += 1

            #   case 3: odd num
                else: 
                    num = (3 * num + 1) // 2
                    cyc_len += 2

        cache[index] = cyc_len
        print(cyc_len)

    """

    return 1


# ------------
# collatz_cycle_length
# ------------

def collatz_cycle_length(num):
    """
    Returns cycle length of num
    """
    cycle_len = 1

    while num is not 1:
        if num % 2 == 0:
            num /= 2
            cycle_len += 1
        else:
            num = num + (num >> 1) + 1
            cycle_len += 2

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
        if val.strip() == "":
            break
        start, end = collatz_read(val)
        mcl = collatz_eval(start, end)
        collatz_print(result, start, end, mcl)
