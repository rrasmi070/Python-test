# a = [1,5,4,4,5]
# b = [3,6,7,7,6]
a = [i for i in input("input a=")]
b = [i for i in input("input b=")]
counts = []
print(a,b)
index_v = 0
temp = None
for i in a:
    print(counts)
    if len(counts) == 0:
        print("------1")
        counts.append(1)
        temp = i
        del a[index_v]
    elif i == temp:
        print("------2")
        incres = int(counts[-1])+1
        counts[-1] = incres
        temp = i
        try:
            del a[index_v]
        except:
            a = []
    else:
        print("------3")
        temp = i
        counts.append(1)
        del a[index_v]

    # temp = i
    # index_v+=1

counts1 = []
# print(len(counts))
index_v1 = 0
temp1 = None
for i in b:
    if len(counts1) == 0:
        counts1.append(1)
        temp1 = i
        del b[index_v1]
    elif i == temp1:
        incres1 = int(counts1[-1])+1
        print(incres1,"----..-")
        counts1[-1] = incres1
        del b[index_v1]
    else:
        temp = i
        counts1.append(1)
        del b[index_v]

print(counts,"=======",counts1)

if counts== counts1:
    print("=======true")
else:
    print("=======false")
