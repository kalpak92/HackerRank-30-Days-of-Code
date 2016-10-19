# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def is_prime(n):
    root = n**.5
    upper = int(math.floor(root) + 1)

    if n == 1:
        return False
    
    elif n == 2:
        return True

    if n % 2 == 0:
        return False

    for div in range(3, upper, 2):
        if n % div == 0:
            return False
    else:
        return True

T = int(input())
for i in range(T):
    data = int(input())
    if is_prime(data):
        print("Prime")
    else:
        print("Not prime")
