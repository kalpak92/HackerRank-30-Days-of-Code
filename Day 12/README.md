# Day 12: Inheritance

## Objective

Today, we're delving into Inheritance. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-inheritance/tutorial) tab for learning materials and an instructional video!

### Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

 - A Student class constructor, which has **4** parameters:
   1. A string, **_firstName_**.
   2. A string, **_lastName_**.
   3. An integer, **_id_**.
   4. An integer array (or vector) of test scores, **_scores_**.
 - A **_char calculate()_** method that calculates a Student object's average and returns the grade character representative of their calculated average: 

 ![](https://github.com/kalpak92/HackerRank-30-Days-of-Code/blob/master/Day%2012/Grading.png)
 

### Input Format

The locked stub code in your editor calls your _Student_ class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

_You are not responsible for reading the following input from stdin_:  
The first line contains **_firstName_**, **_lastName_**, and **_id_**, respectively. The second line contains the number of test scores. The third line of space-separated integers describes **_scores_**.

### Constraints
 - **4 <= | _firstName_ |, | _lastName_ | <= 10**
 - **| _id_ | = 7**
 - **0 <= _score_, _average_ <= 100**

### Output Format

_This is handled by the locked stub code in your editor_. Your output will be correct if your _Student_ class constructor and _calculate()_ method are properly implemented.

### Sample Input
```Python
Heraldo Memelli 8135627
2
100 80
```

### Sample Output
```Python
 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
```

### Explanation

This student had **2** scores to average: **_100_** and **_80_**. The student's average grade is **(100 + 80) / 2  = 90**. An average grade of _90_ corresponds to the letter grade _O_, so our _calculate()_ method should return the character **'O'**.
![](https://github.com/kalpak92/HackerRank-30-Days-of-Code/blob/master/Day%2012/stubCode.png)

