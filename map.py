import math
ex = [9,6,7,8,4,12,11,15]
def unique_len(val,li):
    pass




def gen_random_by_len(leng,prefix_code,exist_code,number_of_codes):
    if int(leng) == 2:
        # random_num1 = [ f"{prefix_code}{str(item)}" for item in random.sample(range(10000000, 39999999), 29999999)]
        # random_num2 = [ f"{prefix_code}{str(item)}" for item in random.sample(range(39999999, 69999999), 29999999)]
        # random_num3 = [ f"{prefix_code}{str(item)}" for item in random.sample(range(69999998, 99999999), 29999999)]
        # lists = [random_num1,random_num2,random_num3]
        # random_num = list(chain(*lists))
        # random_num = [ f"{prefix_code}{str(item)}" for item in random.sample(range(10000000, 99999999), 89999999)]===============
        start,end = 10000000, 99999999
        random_num = gen_unique(prefix_code, start, end, exist_code, number_of_codes)
        
        return random_num
    if int(leng) == 3:
        # random_num = [ f"{prefix_code}{str(item)}" for item in random.sample(range(1000000, 9999999), 8999999)]
        start,end = 1000000, 9999999
        random_num = gen_unique(prefix_code, start, end, exist_code, number_of_codes)
        return random_num
    if int(leng) == 4:
        # random_num = [ f"{prefix_code}{str(item)}" for item in random.sample(range(100000, 999999), 899999)]
        start,end = 100000, 999999
        random_num = gen_unique(prefix_code, start, end, exist_code, number_of_codes)
        return random_num
    if int(leng) == 5:
        # random_num = [ f"{prefix_code}{str(item)}" for item in random.sample(range(10000, 99999), 89999)]
        start,end = 10000, 99999
        random_num = gen_unique(prefix_code, start, end, exist_code, number_of_codes)
        return random_num
        
    if int(leng) == 6:
        # random_num = [ f"{prefix_code}{str(item)}" for item in random.sample(range(1000, 9999), 8999)]
        start,end = 1000, 9999
        random_num = gen_unique(prefix_code, start, end, exist_code, number_of_codes)
        return random_num
