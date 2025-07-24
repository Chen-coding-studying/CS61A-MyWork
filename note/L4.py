def identity(k):
    return k 

def cube(k):
    return pow(k, 3)

def summation(n,term):
    total, k = 0, 1
    while k <= n :
        total, k = total + term(k), k + 1
    return total 








def sum_naturals(n):
    """Sum
   
    total,k = 0,1
    while k <= n:
        total, k = total + k, k + 1
    return total
    """
    return summation(n, identity)




def sum_cubes(n):

    """
    total, k = 0,1
    while k <= n:
        total, k = total + pow(k,3), k + 1
    return total        
    """
    return summation(n,cube)

from operator import mul

def pi_term(k):
    return 8 / mul(4 * k - 3, 4 * k - 1)

print(summation(100000000, pi_term))
