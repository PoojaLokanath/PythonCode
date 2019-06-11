num = int(input("Enter num : "))
c, d = 0, 1
print(c)
for i in range(num-1):
    if c%4 == 0 and c > 8 and c < 500:
        print(c)
    c, d = d, c + d
    
print("======  OR  =========")
    
a, b = 0, 1
while b < 500:
    if b % 4 == 0 and b > 8:
        print(b)
        break
    a, b = b, a+b
    