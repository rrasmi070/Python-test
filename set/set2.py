v= int(input())
b=set()
for i in range(v):
    a = set(map(int, input().split()))
    b.update(a)
print(list(b)[-1])
