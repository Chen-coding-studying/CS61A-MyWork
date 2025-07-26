"""

def at(f,x):
    return f(f(x))

def s(x):
    return x**2

result = at(s,2)

"""



def m_a(n):
    def a(k):
        return k + n
    return a

def s(x):
    return x * x

def tri(x):
    return 3 * x

def composal(f,g):
    def h(x):
        return f(g(x))
    return h

squiple = composal(s, tri)

print()