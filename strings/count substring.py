a = "abcdcdcggcdccdc"
c = 0
inp = 'cdc'
cou = 0
for i in range(len(a)):    
    if str(a[(c):(c+len(inp))]) == inp:
        cou+=1
    c+=1
print(cou)