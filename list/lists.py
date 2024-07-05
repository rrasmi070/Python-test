# from itertools import zip_longest

# if __name__ == '__main__':
#     name_li = []
#     score_li = []
#     for _ in range(int(input())):
#         name = input()
#         name_li.append(name)
#         score = float(input())
#         score_li.append(score)
        
#     aa = sorted(score_li)
#     for i in aa:
#         if i>0:
#             continue
#         else:
#             aa.remove(i)
#     aa = aa[1]
#     li = list(zip_longest(name_li,score_li))
#     nm =[]
#     l = 0
#     for i in range(len(name_li)):
#         l-=1
#         if li[l][1]==aa:
#             nm.append(li[l][0])
#             # print(li[l][0])
    
#     nm = sorted(nm)
#     print(*nm,sep ='\n')


from itertools import zip_longest

if __name__ == '__main__':
    name_li = []
    score_li = []
    for _ in range(int(input())):
        name = input()
        name_li.append(name)
        score = float(input())
        score_li.append(score)
        
    aa = sorted(list(set(score_li)))[1]
    aa = list(set(sorted(score_li)))[1]
    print(aa,"------------------aa")
    li = list(zip_longest(name_li,score_li))
    nm = []
    for i in li:
        if i[1] == aa:
            nm.append(i[0])
    nm = sorted(nm)
    print(*nm,sep ='\n')
    
    
    
'''
4
Prashant
32
Pallavi
36
Dheeraj
39
Shivam
40
-----------------------
'''