#Day 3: Intro to Conditional Statements

## Objective 
In this challenge, we're getting started with conditional statements. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-conditional-statements/tutorial) tab for learning materials and an instructional video!

## Task 
Given an integer, **_n_** , perform the following conditional actions:
- If **_n_** is odd, print **_Weird_**.
- If **_n_** is even and in the inclusive range of **2** to **5** , print **_Not Weird_**.
- If **_n_** is even and in the inclusive range of **6** to **20** , print **_Weird_**.
- If **_n_** is even and greater than **20** , print **_Not Weird_**.

Complete the stub code provided in your editor to print whether or not **_n_**  is weird.

### Input Format

A single line containing a positive integer, **_n_** .

### Constraints

- **1 <= n <= 100**

### Output Format

Print **_Weird_** if the number is weird; otherwise, print **_Not Weird_**.

### Sample Input 0

```Python
3
```

### Sample Output 0

```Python
 Weird
```

### Sample Input 1

```Python
24
```

### Sample Output 1

```Python
  Not Weird
```

### Explanation

_Sample Case 0_: **n = 3**

   **n** is odd and odd numbers are weird, so we print **_Weird_**.

_Sample Case 1_: **n = 24** 

**n > 20** and **n** is even, so it isn't weird. Thus, we print **_Not Weird_**.
