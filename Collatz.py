#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------


EAGER_CACHE = [0] * 1000000
MAX_VAL = 837799  #   value with the largest cycle length in the range
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

    if EAGER_CACHE[1] == 0:
        eager_cache_init()

    first = min(start, end) #   first val in the range
    last = max(start, end) #    last val in the range
    mcl = 0  #   stores the max cycle length

    assert first > 0
    assert last < 1000000
    assert first <= last

    #   max cycle length optimization
    if first <= MAX_VAL <= last :
        return MAX_CL

    middle = (last >> 1) + 1
    if first < middle :
        first = middle

    for num in range(first , last + 1):
        if EAGER_CACHE[num] > mcl:
            mcl = EAGER_CACHE[num]

    return mcl

def eager_cache_init():

    EAGER_CACHE[0] = 0 #    place holder, so cyc len can be looked up directly by value
    EAGER_CACHE[1] = 1
    EAGER_CACHE[2] = 2

    # fill in eager cache with powers of 2
    for power in range(2, 20):
        EAGER_CACHE[2 ** power] = power + 1

    for index in range(3, 1000000):
        if EAGER_CACHE[index] == 0:
            #print("finding cycle len of ", index)
            EAGER_CACHE[index] = collatz_cycle_len(index)

    # print("NUMBER OF VISITS: ", num_of_vists)

# ------------
# collatz_cycle_length
# ------------

def collatz_cycle_len(num):
    """
    Returns cycle length of num
    """

    #   as cycle len of num is calculated, tb (traceback) cache will store values along
    #   the way and use the cycle len of num to determine the cycle len of each of
    #   these values
    #   index is the amount you subtract from the cycle length of the initial input in
    #   order to find the cycle length of the value stored
    tb_cache = [num]
    cycle_len = 1

    assert len(EAGER_CACHE) == 1000000

    while num > 1:

        #   case in which you run into a value already in the eager cache
        if num < len(EAGER_CACHE) and EAGER_CACHE[num] != 0:
            cycle_len = cycle_len + EAGER_CACHE[num] - 1
            num = 1 #   to exit the while loop

        #   even number case
        elif num % 2 == 0:
            num >>= 1   # divide num by 2
            cycle_len += 1
            tb_cache += [num]

        #   odd number case
        else:
            num = num + (num >> 1) + 1
            cycle_len += 2
            tb_cache += [0, num]


    #   going back through traceback_cache and calculated cycle lengths for
    #   each value based on the cycle len of num
    for index, item in enumerate(tb_cache):
        if item < len(EAGER_CACHE) and item != 0 and EAGER_CACHE[item] == 0:
            #print("EAGER_CACHE[", val, "]", "=", cycle_len, "-", index)
            EAGER_CACHE[item] = cycle_len - index

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
    # print("cache filled")
    """
    for index in range(999899, 1000000):
        print(eager_cache[index])
    """

    for val in input_str:
        if not val.strip():
            break

        start, end = collatz_read(val)
        mcl = collatz_eval(start, end)
        collatz_print(result, start, end, mcl)
