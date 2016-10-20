# Day 27: Testing

## Objective 
This challenge is very different from the others we've completed because it requires you to generate a valid test case for a problem instead of solving the problem.  
There is no input to read, you simply have to generate and print test values for the problem that satisfy both the problem's Input Format and the criteria laid out in the Task section. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-testing/tutorial) tab for an instructional video on testing!

### Task 
Create and print a test case for the problem above that meet the following criteria:
 1. **t <= 5**
 2. **1 <= n <= 200**
 3. **1 <= k <= n**
 4. **-10<sup>3</sup> <= a<sub>i</sub> <= 10<sup>3</sup>**, where  **i** belongs to **[1, n]**
 5. The value of **_n_** must be distinct across all the test cases.
 6. Array **_A_** must have at least **1** zero, **1** positive integer, and **1** negative integer.

### Scoring

If you submit **_x_** correct test cases, you will earn **(20.x)%** of the maximum score.  
You _must submit_ **_5_** test cases to earn the maximum possible score.

### Input Format

You are not responsible for reading anything from stdin.

### Output Format

Print **11** lines of output that can be read by the Professor challenge as valid input. Your test case must result in the following output when fed as input to the Professor challenge's solution:
```Python
YES
NO
YES
NO
YES
```
### Explanation
Your code must print lines of output that follow the Input Format in the Professor challenge above. For example, this partial solution to this challenge:
```Python
print('2')
print('4 3')
print('-1 -3 4 2')
print('5 2')
print('0 -1 2 1 4')
```
prints the following output that can be used as valid input for the Professor challenge:
```Python
2
4 3
-1 -3 4 2
5 2
0 -1 2 1 4
```
When read by a valid solution to the Professor challenge, it produces the following output:
```Python
YES
NO
```
You must do something similar to this, except that the test case you develop must meet the constraints set in the Task section above.