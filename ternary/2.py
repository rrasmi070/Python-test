a=list('1234567890')
b = [i for i in a if int(i) % 2]
print(b)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)