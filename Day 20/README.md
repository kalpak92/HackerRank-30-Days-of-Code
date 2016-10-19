# Day 20: Sorting

## Objective 
Today, we're discussing a simple sorting algorithm called _Bubble Sort_. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-sorting/tutorial) tab for learning materials and an instructional video!  

Consider the following version of Bubble Sort:
```Java
for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
```
### Task 
Given an array, **a**, of size **n** containing distinct elements **a[0], a[1],..., a[n -1]**, sort array **a** in ascending order using the _Bubble Sort_ algorithm above. Once sorted, print the following  lines:
 1. Array is sorted in **_numSwaps_** swaps   
 where _numSwaps_ is the number of swaps that took place.

 2. First Element: **_firstElement_**  
    where _firstElement_ is the first element in the sorted array.
 3. Last Element: **_lastElement_**  
    where _lastElement_ is the last element in the sorted array.

**Hint**: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

### Input Format

The first line contains an integer, **_n_**, denoting the number of elements in array **_a_**.   
The second line contains **_n_** space-separated integers describing **_a_**, where the **_i<sup>th</sup>_** integer is **a[i]**, **_i_** belongs to **[0, n - 1]**.

### Constraints

 - **2 <= n <= 600**
 - **1 <= a[i] <= 2 x 10 <sup>6</sup>**, **_i_** belongs to **[0, n - 1]**.

### Output Format

There should be  lines of output:
 1. Array is sorted in **_numSwaps_** swaps   
 where _numSwaps_ is the number of swaps that took place.

 2. First Element: **_firstElement_**  
    where _firstElement_ is the first element in the sorted array.
 3. Last Element: **_lastElement_**  
    where _lastElement_ is the last element in the sorted array.

### Sample Input 0
```Python
3
1 2 3
```
### Sample Output 0
```Python
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
```

### Sample Input 1
```Python
3
3 2 1
```
### Sample Output 1
```Python
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
```
### Explanation
![](https://github.com/kalpak92/HackerRank-30-Days-of-Code/blob/master/Day%2020/explanation.PNG)
