n = int(input())
A = set(map(int, input().split()))
m = int(input())
for i in range(m):
    update_v, *arg = input().split()
    o_li = set(map(int, input().split()))
    if update_v=='intersection_update':
        try:
            A.intersection_update(set(o_li))
        except:
            continue
    elif update_v=='symmetric_difference_update':
        try:
            A.symmetric_difference_update(set(o_li))
        except:
            continue
    elif update_v=='difference_update':
        try:
            A.difference_update(set(o_li))
        except:
            continue
    else:
        continue
print(sum(A))



n = int(input())
s = set(map(int, input().split()))
q = int(input())

# perform the set operations based on the input queries
for i in range(q):
    query = input().split()
    if query[0] == "intersection_update":
        other_set = set(map(int, input().split()))
        s.intersection_update(other_set)
    elif query[0] == "update":
        other_set = set(map(int, input().split()))
        s.update(other_set)
    elif query[0] == "symmetric_difference_update":
        other_set = set(map(int, input().split()))
        s.symmetric_difference_update(other_set)
    elif query[0] == "difference_update":
        other_set = set(map(int, input().split()))
        s.difference_update(other_set)

# print the sum of the elements in the final set
print(sum(s))
