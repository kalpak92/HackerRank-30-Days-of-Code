# Day 19: Interfaces

## Objective 
Today, we're learning about Interfaces. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-interfaces/tutorial) tab for learning materials and an instructional video!

### Task 
The **_AdvancedArithmetic_** interface and the method declaration for the abstract **_int divisorSum(int n)_** method are provided for you in the editor below.  
Write the _Calculator_ class, which implements the _AdvancedArithmetic_ interface. The implementation for the _divisorSum_ method must be public and take an integer parameter, _n_, and return the sum of all its divisors.

**Note**: Because we are writing multiple classes in the same file, do not use an access modifier (e.g.: public) in your _class declaration_ (or your code will not compile); however, you must use the _public_ access modifier before your _method declaration_ for it to be accessible by the other classes in the file.

### Input Format

A single line containing an integer, **_n_**.

### Constraints

 - **1 <= n <= 1000**

### Output Format

You are not responsible for printing anything to stdout. The locked _Solution_ class in the editor below will call your code and print the necessary output.

### Sample Input
```Python
6
```
### Sample Output
```Python
I implemented: AdvancedArithmetic
12
```

### Explanation
The integer **6** is evenly divisible by **1**, **2**, **3**, and **6**. Our _divisorSum_ method should return the sum of these numbers, which is **1 + 2 + 3 + 6 = 12**. The Solution class then prints **I immplemented: AdvancedArithmetic** on the first line, followed by the sum returned by divisorSum (which is **12**) on the second line.
