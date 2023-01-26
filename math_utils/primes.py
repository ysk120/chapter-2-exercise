from math import sqrt

def isprime(n):
    flag = 0
    if n > 1:
        for k in range(2, int(sqrt(n))+1):
            if (n % k == 0):
                flag = 1
            break
        if flag == 0:
            return True
        else:
            return False
    else:
        return False
