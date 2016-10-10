
# Day 16: Exceptions - String to Integer

## Objective 
Today, we're getting started with Exceptions by learning how to parse an integer from a string and print a custom error message. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/tutorial) tab for learning materials and an instructional video!

### Task 
Read a string, _**S**_, and print its integer value; if **_S_** cannot be converted to an integer, print **Bad String**.

**Note**: You must use the _String-to-Integer_ and exception handling constructs built into your submission language. If you attempt to use loops/conditional statements, you will get a _0_ score.

### Input Format

A single string, **_S_**.

### Constraints
 - **1 <= | S | <= 6, where | S | is the length of the string S.**
 - _S_ is either composed of lowercase letters (_a - z_) or decimal digits (_0 - 9_).

### Output Format

Print the parsed integer value of _S_, or _Bad String_ if _S_ cannot be converted to an integer.

### Sample Input 0
```Python
3
```
### Sample Output 0
```Python
3
```
### Sample Input 1
```Python
za
```
### Sample Output 1
```Python
Bad String
```
### Explanation

Sample Case _0_ contains an integer, so it should not raise an exception when we attempt to convert it to an integer. Thus, we print the **3**.  
Sample Case _1_ does not contain any integers, so an attempt ot convert it to an integer will raise an exception. Thus, our exception handler prints **Bad String**.
