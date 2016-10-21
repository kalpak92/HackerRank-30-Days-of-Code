# Day 28: RegEx, Patterns, and Intro to Databases

## Objective 
Today, we're working with regular expressions. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-regex-patterns/tutorial) tab for learning materials and an instructional video!

### Task 
Consider a database table, Emails, which has the attributes First Name and Email ID. Given **_N_** rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in **_gmail.com_**.

### Input Format

The first line contains an integer, **N**, total number of rows in the table.  
Each of the **N** subsequent lines contains **2** space-separated strings denoting a person's first name and email ID, respectively.
### Constraints
 - **_2 <= N <= 30_**
 - Each of the first names consists of lower case letters [a - z] only.
 - Each of the email IDs consists of lower case letters [a - z], **@** and **.** only.
 - The length of the first name is no longer than 20.
 - The length of the email ID is no longer than 50.

### Output Format

Print an alphabetically-ordered list of first names for every user with a gmail account. Each name must be printed on a new line.

### Sample Input
```Python
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
```
### Sample Output
```Python
julia
julia
riya
samantha
tanya
```