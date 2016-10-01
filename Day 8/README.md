# Day 8: Dictionaries and Maps

## Objective 
Today, we're learning about _Key-Value pair mappings_ using a Map or Dictionary data structure. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-dictionaries-and-maps/tutorial) tab for learning materials and an instructional video!

### Task

Given **_n_** names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each **_name_** queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for **_name_** is not found, print Not found instead.

**Note**: Your phone book should be a Dictionary/Map/HashMap data structure.

### Input Format

The first line contains an integer, **_n_** , denoting the number of entries in the phone book. 
Each of the **_n_** subsequent lines describes an entry in the form of **2** space-separated values on a single line. The first value is a friend's name, and the second value is an **8**-digit phone number.

After the **n** lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a **_name_** to look up, and you must continue reading lines until there is no more input.

**Note**: Names consist of lowercase English alphabetic letters and are first names only.

### Constraints

- **_1 <= n <= 10<sup>5</sup>_**
- **_1 <= queries <= 10<sup>5</sup>_**

### Output Format

On a new line for each query, print Not found if the name has no corresponding entry in the phone book; otherwise, print the full **_name_** and **_phoneNumbe_r** in the format name=phoneNumber.

### Sample Input

```Python
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
```

### Sample Output
```Python
sam=99912222
Not found
harry=12299933
```

### Explanation
![](https://github.com/kalpak92/HackerRank-30-Days-of-Code/blob/master/Day%208/explanation.png)

