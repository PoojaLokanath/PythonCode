from numpy import linspace
num = int(input("Enter int :"))
data = linspace(1, 2, num)
for x in data:
    print(x)

print("-----------")

a = int(input("Enter int :"))
b = 1.0/(a-1)
x = 0.0

while x < (1.0-b/2):
    print(x)
    x = x + b
print(1.0)