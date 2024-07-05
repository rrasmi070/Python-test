from itertools import cycle, compress, groupby, accumulate, product
# for i in count(10,0.5):
#     print(i)
#     if i > 20:
#         break

# for i in range(2,20,5):
#     print(i)
#     if i > 20:
#         break

# negative value vetween 0 to 5
# n = 0
# for i in range(5):
#     print(n)
#     n-=1

# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
# for color in cycle(colors):
#     print(color)

# shapes = ['circle', 'triangle', 'square', 'pentagon']
# selections = [True, False, True, False]
# result = compress(shapes, selections)
# print(result,"------------")
# for each in result:
#     print(each)


# robots = [
#     {"name": "blaster", "faction": "autobot"},
#     {"name": "galvatron", "faction": "decepticon"},
#     {"name": "jazz", "faction": "autobot"},
#     {"name": "metroplex", "faction": "autobot"},
#     {"name": "megatron", "faction": "decepticon"},
#     {"name": "starcream", "faction": "decepticon"},
# ]
# z= groupby(robots, key=lambda x: x['faction'])
# print(list(z))
# for key, group in groupby(robots, key=lambda x: x['faction']):
#     # print(key)
#     print(list(group))

a = b= [2,3,1,4,5,6,2]
print(a,"-----------", b)