# Day 26: Nested Logic

## Objective 
Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge to complete this challenge, but check out the [Tutorial](https://www.hackerrank.com/challenges/30-nested-logic/tutorial) tab for a video on testing!

### Task 
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

 1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: **_fine = 0_**).
 2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, **_fine = 15 Hackos * no. of days late_**.
 3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the **_fine = 500 Hackos * no. of months late_**.
 4. If the book is returned after the calendar **_year_** in which it was expected, there is a fixed fine of **_10000 Hackos_**.


### Input Format

The first line contains  space-separated integers denoting the respective _day_, _month_, and _year_ on which the book was **_actually returned_**.   
The second line contains  space-separated integers denoting the respective  _day_, _month_ and _year_ on which the book was **_expected to be returned_** (due date).

### Constraints

 - **1 <= D <= 31**
 - **1 <= M <= 12**
 - **1 <= Y <= 3000**
 - **It is guaranteed that dates will be valid Gregorian Calendar dates.**

### Output Format

Print a single integer denoting the library fine for the book received as input.

### Sample Input
```Python
9 6 2015
6 6 2015
```

### Sample Output
```Python
45
```

### Explanation

![](https://github.com/kalpak92/HackerRank-30-Days-of-Code/blob/master/Day%2026/explanation.PNG)
