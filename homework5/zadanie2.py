def a(n):
   if n<2: return 1
   return n*a(n-1)

def b(n):
    if n == 0: return 0
    if n%2 == 1: return n + b(n - 1)
    else: return b(n-1)

def c(n):
    if n == 0: return 0
    if n%3 == 0: return n + b(n - 1)
    else: return b(n-1)

def d(n):
    if n == 0: return 0
    return 2*n+3 + d(n-1)

def e(n):
    if n == 0: return 0
    if n == 1: return 1
    return 3*e(n-1) - e(n-2)


print(a(7))
print(b(7))
print(c(7))
print(d(7))
print(e(7))

