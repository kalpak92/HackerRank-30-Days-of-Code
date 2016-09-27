# Day 4: Class vs. Instance


## Objective 
In this challenge, we're going to learn about the difference between a _class_ and _an instance_; because this is an **_Object Oriented concept_**, it's only enabled in certain languages. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-class-vs-instance/tutorial) tab for learning materials and an instructional video!

## Task 
Write a _Person_ class with an instance variable, **_age_**, and a constructor that takes an integer, **_initialAge_**, as a parameter. The constructor must assign **_initialAge_** to **_age_** after confirming the argument passed as **_initialAge_**  is not negative; if a negative argument is passed as **_initialAge_**, the constructor should set **_age_** to **_0_** and print **Age is not valid, setting age to 0**.

In addition, you must write the following instance methods:
1. **_yearPasses()_** should increase the **_age_** instance variable by **_1_**.
2. **_amIOld()_** should perform the following conditional actions:

	- If **_age < 13_**, print **You are young.**.
	- If **_age >= 13_** and **_age < 18_**, print **You are a teenager.**.
	- Otherwise, print **You are old.**.

To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. The code that creates each instance of your Person class is in the main method. Don't worry if you don't understand it all quite yet!

**Note**: Do not remove or alter the stub code in the editor.


### Input Format

Input is handled for you by the stub code in the editor.

The first line contains an integer, **_T_** (the number of test cases), and the **_T_** subsequent lines each contain an integer denoting the **_age_** of a Person instance.

### Constraints

- **1 <= T <= 4**
- **-5 <= _age_ <= 30**

### Output Format

Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print **2** or **3** lines (depending on whether or not a valid **_initialAge_** was passed to the constructor).

### Sample Input 0

```Python
4
-1
10
16
18
```

### Sample Output 0

```Python
Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
```

### Explanation

Test Case 0: **_initialAge = -1_**
	
Because **_initialAge < 0_**, our code must set **age** to **0** and print the "**Age is not valid..**" message followed by the young message. Three years pass and **_age = 3_**, so we print the young message again.

Test Case 1: **_initialAge = 10_** 

Because **_initialAge < 13_**, our code should print that the person is young. Three years pass and **_age = 13_**, so we print that the person is now a teenager.

Test Case 2: **_initialAge = 16_**

Because , **_13 <= initialAge < 18_**, our code should print that the person is a teenager. Three years pass and **_age = 19_**, so we print that the person is old.

Test Case 3: **_initialAge = 18_**  

Because **_initialAge >= 18_**, our code should print that the person is old. Three years pass and the person is still old at **_age = 21_**, so we print the old message again.


**The extra line at the end of the output is supposed to be there and is trimmed before being compared against the test case's expected output. If you're failing this challenge, check your logic and review your print statements for spelling errors.**

![alt text](https://github.com/kalpak92/HackerRank-30-Days-of-Code/blob/master/Day%204/explanation.PNG "Explanation")
