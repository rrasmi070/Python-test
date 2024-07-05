import random


gen_len = 10
li = []
ex = [1,2,4,3,7,5,6,9,8]
while len(li) < gen_len+1:
    # print(len(li),"iiiiiii")
    ran_val = random.randint(0,30)
    # li = [ran_val if ran_val not in ex else None]
    if ran_val not in ex:
        li.append(ran_val)
    # else:
    #     None
    
ex.sort()
        
print(li)