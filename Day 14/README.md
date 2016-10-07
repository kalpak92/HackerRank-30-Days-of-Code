# Day 14: Scope

## Objective 
Today we're discussing scope. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-scope/tutorial) tab for learning materials and an instructional video!

The _absolute difference_ between two integers, _a_ and _b_, is written as _|a - b|_. The _maximum absolute difference_ between two integers in a set of positive integers, _elements_, is the largest absolute difference between any two integers in _elements_.

The **_Difference_** class is started for you in the editor. It has a private integer array (_elements_) for storing _N_ non-negative integers, and a public integer (_maximumDifference_) for storing the maximum absolute difference.

### Task 
Complete the _Difference_ class by writing the following:

 - A class constructor that takes an array of integers as a parameter and saves it to the _elements_ instance variable.
 - A _computeDifference_ method that finds the maximum absolute difference between any **_2_** numbers in **_N_** and stores it in the _maximumDifference_ instance variable.

### Input Format

You are not responsible for reading any input from stdin. The locked _Solution_ class in your editor reads in **2** lines of input; the first line contains **N**, and the second line describes the _elements_ array.

### Constraints

 - **1 <= N <= 10**
 - **1 <= _elements_[_i_] <= 100, where 0 <= i <= N - 1**

### Output Format

You are not responsible for printing any output; the _Solution_ class will print the value of the _maximumDifference_  instance variable.

### Sample Input
```Python
3
1 2 5
```
### Sample Output
```Python
4
```

### Explanation

The scope of the _elements_ array and _maximumDifference_ integer is the entire class instance. The class constructor saves the argument passed to the constructor as the _elements_ instance variable (where the computeDifference method can access it).

To find the maximum difference, computeDifference checks each element in the array and finds the maximum difference between any **_2_** elements:  
**|1 - 2| = 1  
|1 - 5| = 4  
|2 - 5| = 3** 

The maximum of these differences is **4**, so it saves the value **4** as the _maximumDifference_ instance variable. The locked stub code in the editor then prints the value stored as _maximumDifference_, which is **4**.