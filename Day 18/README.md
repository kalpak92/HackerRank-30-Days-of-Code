# Day 18: Queues and Stacks

Welcome to Day 18! Today we're learning about Stacks and Queues. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-queues-stacks/tutorial) tab for learning materials and an instructional video!

A **_palindrome_** is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards. Can you determine if a given string, , is a palindrome?

To solve this challenge, we must first take each character in _s_, _enqueue_ it in a _queue_, and also push that same character onto a _stack_. Once that's done, we must _dequeue_ the first character from the _queue_ and _pop_ the top character off the _stack_, then compare the two characters to see if they are the same; as long as the characters match, we continue dequeueing, popping, and comparing each character until our containers are empty (a non-match means _s_ isn't a palindrome).

Write the following declarations and implementations:

 1. Two instance variables: one for your **_stack_**, and one for your **_queue_**.  
 2. A **_void pushCharacter(char ch)_** method that pushes a character onto a stack.
 3. A **_void enqueueCharacter(char ch)_** method that enqueues a character in the **_queue_** instance variable.
 4. A **_char popCharacter()_** method that pops and returns the character at the top of the **_stack_** instance variable.
 5. A **_char dequeueCharacter()_** method that dequeues and returns the first character in the **_queue_** instance variable.

### Input Format

You do not need to read anything from stdin. The locked stub code in your editor reads a single line containing string **_s_**. It then calls the methods specified above to pass each character to your instance variables.

### Constraints

 - _**s**_ is composed of lowercase English letters.

### Output Format

You are not responsible for printing any output to stdout.   
If your code is correctly written and **_s_** is a palindrome, the locked stub code will print _The word, **s**, is a palindrome._; otherwise, it will print _The word, **s**, is not a palindrome._ 

### Sample Input
```Python
racecar
```
### Sample Output
```Python
The word, racecar, is a palindrome.
```