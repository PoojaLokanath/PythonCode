f = open('pendulum.txt')

out = open('col2.txt', 'w')

for line in f:
    fields = line.split()
    print(fields[1], file=out)
f.close()
out.close()

print("=========")

f = open('pendulum.txt')

out = open('col2.txt', 'w')

for line in f:
    fields = line.split()
    out.write(fields[1] + '\n')
f.close()
out.close()