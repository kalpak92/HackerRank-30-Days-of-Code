#!/bin/python3

import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

def hourglass_sum(arr, i, j):
    sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] # top horizontal
    i += 1
    sum += arr[i][j + 1]                            # middle
    i += 1
    sum += arr[i][j] + arr[i][j + 1] + arr[i][j + 2] # bottom horizontal
    return sum

def max_hourglasses(arr):
    max = -9 * 36            # Given as constraint that the minimum value of A[i][j] can be -9
    for i in range(0, 4):
        for j in range(0, 4):
            sum = hourglass_sum(arr, i, j)
            #print(sum)
            if sum > max:
                max = sum
    return max

print(max_hourglasses(arr))