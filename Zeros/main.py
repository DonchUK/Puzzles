#!/usr/bin/env python3

import sys


def get_values_from_file(file, limit):
    with open(file, 'r') as input_file:
        for line in input_file:
            if len(line) != 1 and len(line.split()) == 2:
                N = int(line.split()[0])
                K = int(line.split()[1])
                if N | K > limit:
                    print(f"Values aren't valid: N = {N}, K = {K}.\nPlease write correct values in input file.")
                    sys.exit(0)
                return N, K
            else:
                print("Number of params != 2. \nPlease write correct input file.")
                sys.exit(0)


def get_number_coincidences(n, k):
    c = 0
    for i in range(1, n):
        if str(bin(i)).replace('0b', '').count('0') == k:
            c += 1
    return str(c)


def write_value_in_output_file(file, value):
    with open(file, 'w') as output_file:
        output_file.write(value)


if __name__ == '__main__':
    max_value = 10 ** 9
    path_to_input_file = 'Files/INPUT.TXT'
    path_to_output_file = 'Files/OUTPUT.TXT'

    N, K = get_values_from_file(path_to_input_file, max_value)
    write_value_in_output_file(path_to_output_file, get_number_coincidences(N, K))
