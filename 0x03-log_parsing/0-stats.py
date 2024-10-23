#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """

import sys


def print_metrics(status_counts, total_size):
    """ Prints information """
    print("File size: {:d}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] != 0:
            print("{}: {:d}".format(code, status_counts[code]))


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}

line_count = 0
total_size = 0

try:
    for log_line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            print_metrics(status_codes, total_size)

        log_parts = log_line.split()
        line_count += 1

        try:
            total_size += int(log_parts[-1])
        except (ValueError, IndexError):
            pass

        try:
            if log_parts[-2] in status_codes:
                status_codes[log_parts[-2]] += 1
        except IndexError:
            pass
    print_metrics(status_codes, total_size)

except KeyboardInterrupt:
    print_metrics(status_codes, total_size)
    raise