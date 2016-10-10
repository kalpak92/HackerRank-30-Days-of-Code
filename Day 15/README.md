# Day 15: Linked List

## Objective 
Today we're working with Linked Lists. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-linked-list/tutorial) tab for learning materials and an instructional video!#

A _Node_ class is provided for you in the editor. A _Node_ object has an integer data field, _data_, and a _Node_ instance pointer, _next_, pointing to another node (i.e.: the next node in a list).

A _Node **insert**_ function is also declared in your editor. It has two parameters: a pointer, _**head**_, pointing to the first node of a linked list, and an integer **_data_** value that must be added to the end of the list as a new _Node_ object.

### Task 
Complete the insert function in your editor so that it creates a new Node (pass _data_ as the Node constructor argument) and inserts it at the tail of the linked list referenced by the _head_ parameter. Once the new node is added, return the reference to the _head_ node.

**Note**: If the **_head_** argument passed to the insert function is _null_, then the initial list is empty.

### Input Format

The _insert_ function has **2** parameters: a pointer to a _Node_ named _head_, and an integer value, _data_. 
The constructor for Node has **1** parameter: an integer value for the _data_ field.

You do not need to read anything from stdin.

### Output Format

Your insert function should return a reference to the _head_ node of the linked list.

### Sample Input

The following input is handled for you by the locked code in the editor: 
The first line contains T, the number of test cases. 
The _T_ subsequent lines of test cases each contain an integer to be inserted at the list's tail.
```Python
4
2
3
4
1
```

### Sample Output

The locked code in your editor prints the ordered data values for each element in your list as a single line of space-separated integers:
```Python
2 3 4 1
```

### Explanation

![](https://github.com/kalpak92/HackerRank-30-Days-of-Code/blob/master/Day%2015/expanation.png)

![](https://github.com/kalpak92/HackerRank-30-Days-of-Code/blob/master/Day%2015/snippet.png)
