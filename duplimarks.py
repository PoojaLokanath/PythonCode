
d = {'Pooja' : 90, 'MAnali' : 60}

allmark = list(d.values())

unique = set(allmark)

dupli = len(allmark) - len(unique)
print(dupli, 'duplicate')


print("=======")

n = int(input())
result = []

for i in range(1, n, 2):
    result.append(i*i)
print (result)