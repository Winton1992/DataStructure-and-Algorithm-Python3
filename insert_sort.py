def insert_sort(list):
    count = len(list)
    for i in range(1, count):
        key = list[i]
        j = i - 1
        while j >= 0:
            if list[j] > key:
                list[j + 1] = list[j]
                list[j] = key
            j -= 1   # 使其跳出while循环
    return list

#test
list=[10,23,1,53,654,54,16,646,65,3155,546,31]
print (insert_sort(list))