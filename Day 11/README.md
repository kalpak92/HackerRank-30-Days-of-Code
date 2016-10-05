# Day 11: 2D Arrays

## Objective

Today, we're building on our knowledge of Arrays by adding another dimension. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-2d-arrays/tutorial) tab for learning materials and an instructional video!

#### Context 
Given a **_6x6_** 2D Array, _A_:
```Python
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```

We define an hourglass in _A_ to be a subset of values with indices falling in this pattern in _A_'s graphical representation:
```Python
a b c
  d
e f g
```
There are **_16_** hourglasses in _A_, and an _hourglass sum_ is the sum of an hourglass' values.

### Task
Calculate the hourglass sum for every hourglass in _A_, then print the **_maximum hourglass sum_**.

### Input Format

There are **6** lines of input, where each line contains _6_ space-separated integers describing 2D Array _A_; every value in A will be in the inclusive range of **-9 to 9**.

### Constraints
 - **-9 <= A[i][j] <= 9**
 - **0 <= _i_, _j_ <= 5**

### Output Format

Print the largest (maximum) hourglass sum found in _A_.

### Sample Input
```Python
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
```

### Sample Output
```Python
19
```

### Explanation

_A_ contains the following hourglasses:
```Python
1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
```

The hourglass with the maximum sum (_19_) is:
```Python
2 4 4
  2
1 2 4
```
