n = int(input('n='))

a = []
s = input()
a = s.split(" ")

a1 = int(input())
a2 = int(input())

for i in range(n):
    a[i] = int(a[i])

min = a[0]

for i in range(n):
    if min > a[i]:
        min = a[i]

for i in range(n):
    if a1-1 <= i <= a2-1:
        a[i] = a[i] / min
        print(a[i])
    else:
        print(a[i])
