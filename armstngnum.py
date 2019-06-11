num = input("Enter number")
num = int(num)
a = num // 100
b = (num % 100) // 10
c = num % 10

print((a**3 + b**3 + c**3) == num)

print("2nd num")
num = input("Enter num")
num = int(num)

a = num // 100
b = (num % 100) // 10
c = num % 10

A = a * a * a
B = b * b * b
C = c * c * c

print(A)
print(B)
print(C)
