a, b = 0, 1
while b < 500:
    if b % 4 == 0:
        print(b)
        break
    a, b = b, a + b
    
print('2nd Code :')
    
for i in range(5):
    if i % 2 == 0:
        pass
    else:
        print(i, 'is odd')
        
print('3rd Code : ')
        
for n in range(1, 10, 2):
    if n%3 == 0:
        continue
    print(n*n) 