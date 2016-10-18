# Day 17: More Exceptions

## Objective  
Yesterday's challenge taught you to manage exceptional situations by using try and catch blocks. In today's challenge, you're going to practice throwing and propagating an exception. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-more-exceptions/tutorial) tab for learning materials and an instructional video!

### Task 
Write a _**Calculator**_ class with a single method: **_int power(int,int)_**. The _power_ method takes two integers, **n** and **p**, as parameters and returns the integer result of **_n<sup>p</sup>_**. If either _n_ or _p_ is negative, then the method must throw an exception with the message: **n and p should be non-negative.**

**Note**: Do not use an access modifier (e.g.: public) in the declaration for your _Calculator_ class.

### Input Format

Input from stdin is handled for you by the locked stub code in your editor. The first line contains an integer, **_T_**, the number of test cases. Each of the **_T_** subsequent lines describes a test case in **2** space-separated integers denoting _n_ and _p_, respectively.

### Constraints

 - No Test Case will result in overflow for correctly written code.

### Output Format

Output to stdout is handled for you by the locked stub code in your editor. There are **_T_** lines of output, where each line contains the result of **_n<sup>p</sup>_** as calculated by your _Calculator_ class' _power_ method.

### Sample Input
```Python
4
3 5
2 4
-1 -2
-1 3
```
### Sample Output
```Python
243
16
n and p should be non-negative
n and p should be non-negative
```

### Explanation
**_T = 4_**  
**T<sub>0</sub>**: **3** and **5** are positive, so power returns the result of **3<sup>5</sup>**, which is **243**.  

**T<sub>1</sub>**: **2** and **4** are positive, so power returns the result of **2<sup>4</sup>**, which is **16**.  

**T<sub>2</sub>**: Both inputs (**-1** and **-2**) are negative, so power throws an exception and **n and p should be non-negative** is printed.   

**T<sub>3</sub>**: One of the inputs (**-1**) is negative, so power throws an exception and **n and p should be non-negative** is printed.
