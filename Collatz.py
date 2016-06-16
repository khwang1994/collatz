#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

eager_cache = [0] * 1000000

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

    first = min(start, end) #   first val in the range
    last = max(start, end) #    last val in the range
    mcl = eager_cache[first]    #   stores the max cycle length

    assert first > 0 
    assert last < 1000000
    assert first <= last 

    for num in range(first + 1, last + 1):
        if eager_cache[num] > mcl:
            mcl = eager_cache[num]

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

    return mcl

def eager_cache_init(val):

    eager_cache[0] = 0 #    place holder, so cyc len can be looked up directly by value
    eager_cache[1] = 1
    eager_cache[2] = 2

    # fill in eager cache with powers of 2
    for power in range(2, 20):
        eager_cache[2 ** power] = power + 1

    for index in range(3, 1000000):
        if eager_cache[index] == 0:
            print("finding cycle len of ", index)
            eager_cache[index] = collatz_cycle_len(index)

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

    assert len(eager_cache) == 1000000

    while num > 1:

        #   case in which you run into a value already in the eager cache
        if num < len(eager_cache) and eager_cache[num] != 0: 
                cycle_len = cycle_len + eager_cache[int(num)] - 1
                num = 1
        #   even number case
        elif num % 2 == 0:
            num = num // 2
            cycle_len += 1
            tb_cache += [num]

        #   odd number case
        else:
            num = (3 * num + 1) // 2
            cycle_len += 2
            tb_cache += [0, num]

    #   going back through traceback_cache and calculated cycle lengths for
    #   each value based on the cycle len of num
    for index in range(len(tb_cache)):
        #print(tb_cache)
        val = tb_cache[index]
        if val < len(eager_cache) and val != 0 and eager_cache[val] == 0:  # value must be within the given bounds
            # print("eager_cache[", val, "]", "=", cycle_len, "-", index)
            eager_cache[val] = cycle_len - index

    """
    for index in range(0, 21):
        print(eager_cache[index])
    """

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

    random = eager_cache_init(0)

    assert eager_cache[4] is 3
    #assert eager_cache[8] is 4

    print("cache filled")

    for val in input_str:
        if not val.strip():
            break

        start, end = collatz_read(val)
        mcl = collatz_eval(start, end)
        collatz_print(result, start, end, mcl)
