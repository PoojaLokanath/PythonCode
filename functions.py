def what(x, n):
    if n < 0:
        n = -n
        x = 1.0 / x
    z = 1.0
    while n > 0:
        if n%2 == 1:
            z *= x
        x *= x
        n //= 2
    return z
    
print("=============")

def prompt():
    name = input()
    print('Hello', name)
prompt()
#input --> Shanbhag
#output --> Hello Shanbhag
    
print("=============")

def prompt1():
    name = 'Pooja'
    print('Hello', name)
prompt1()
#output --> Hello Pooja

print("=============")

def add(a, b):
    sum = a + b
    return(sum)
add(8, 2)
    #output --> 10

print("=============")
    
def add1(a, b):
    return(a + b)
add1(5, 7)
#output --> 12

print("=============")

def is_even(n):    
    if n%2 == 0:
        return True
    else:
        return False
is_even(5)
#output --> True

print("=============")

def is_even(n):
    return n%2 == 0
is_even(10)
#output --> True

print("=============")

def even_square(n):
    if n%2==0:
        return True,n*n
    else:
        return False,n*n
even_square(2)
#output --> True 4

print("=============")

def even_square(x):
    return x%2 == 0, x*x
even_square(3)
#output --> False 9

print("=============")

def greet(name, msg='hello'):
    return msg+ ' ' + name
greet('poo', 'hi')
#output --> hi poo
#output1 --> hello poo (default)

print("=============")

def to_lower(name):
    return name.lower()
to_lower('SHANBHAG')
#output --> shanbhag

print("=============")

def to_lower(data):
    result = []
    for x in data:
        result.append(x.lower())
    return result
to_lower('POOJA')
#output --> ['p', 'o', 'o', 'j', 'a']

print("=============")

def power2():
    def f(x):
        return 2**x
    return f
power2()(4)
#output --> 16

print("=============")

def power(n=2):
    def f(x):
        return n**x
    return f
power(2)(3)
#output --> 8

print("=============")

def apply(f, data):
    def f(x):
        return 2*x
    result = []
    for x in data:
        result.append(f(x))
    return result
apply(f, [1, 2, 3])
#output --> [2, 4, 6]

print("========================")

def my_sum(s):
    total = 0
    for word in s.split():
        try:
            total += int(word)
        except ValueError:
            pass
    return total
#output --> my_sum('HII 1 how are ypu 2 im fine 3')
            # 6