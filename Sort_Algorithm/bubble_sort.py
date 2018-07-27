def bubble_sort(list):
    length=len(list)
    for index in range(length):  # if length is 5, then index will be 0 1 2 3 4
        for i in range(1,length-index):
            if list[i-1]<list[i]:
                list[i],list[i-1]=list[i-1],list[i] # change position
    return list

list=[10,23,1,53,654,54,16,646,65,3155,546,31]
print (bubble_sort(list))