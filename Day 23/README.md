# Day 23: BST Level-Order Traversal

## Objective 
Today, we're going further with Binary Search Trees. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-binary-trees/tutorial) tab for learning materials and an instructional video!

### Task 
A _level-order traversal_, also known as a **breadth-first search**, visits each level of a tree's nodes from left to right, top to bottom. You are given a pointer, **_root_**, pointing to the root of a binary search tree. Complete the _levelOrder_ function provided in your editor so that it prints the level-order traversal of the binary search tree.

**Hint**: You'll find a queue helpful in completing this challenge.


### Input Format

The locked stub code in your editor reads the following inputs and assembles them into a BST: 
The first line contains an integer, **_T_** (the number of test cases). 
The **_T_** subsequent lines each contain an integer, **_data_**, denoting the value of an element that must be added to the BST.

### Output Format

Print the **_data_** value of each node in the tree's level-order traversal as a single line of **N** space-separated integers.

### Sample Input
```Python
6
3
5
4
7
2
1
```

### Sample Output
```Python
3 2 5 1 4 7 
```

### Explanation

The input forms the following binary search tree:   
![](https://github.com/kalpak92/HackerRank-30-Days-of-Code/blob/master/Day%2023/explanation.PNG)  

We traverse each level of the tree from the root downward, and we process the nodes at each level from left to right. The resulting level-order traversal is **3 -> 2 -> 5 -> 1 -> 4 -> 7**, and we print these data values as a single line of space-separated integers.
