"""Approximate pi with the Bailey-Borwein-Plouffe formula.

Adapted from:
http://blog.recursiveprocess.com/2013/03/14/calculate-pi-with-python
"""

import sys
from decimal import Decimal


def bailey_borwein_plouffe_formula(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1) / (16**k)) * (
            (Decimal(4) / (8 * k + 1))
            - (Decimal(2) / (8 * k + 4))
            - (Decimal(1) / (8 * k + 5))
            - (Decimal(1) / (8 * k + 6))
        )
        k += 1
    return pi


if __name__ == "__main__":
    for i in range(1, int(sys.argv[1])):
        print(i, bailey_borwein_plouffe_formula(i))
