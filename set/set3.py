a = int(input())
for i in range(a):
    b = int(input(""))
    set1 = list(map(int, input().split(" ")))
    c = int(input())
    set2 = set(map(int, input().split()))
    if set2.issubset(set1):
        
        print(True)
    else:
        print(False)
