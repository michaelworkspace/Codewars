import math


def f(n, m):
# Naive approach
# 	total = 0
# 	for i in range(1, n+1):
# 		total += i % m
# 	return total
#
# One-liner approach
    return math.floor(n/m) * (m-1) * m/2 + (n%m) * (n%m+1) / 2;
