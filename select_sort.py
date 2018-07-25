def select_sort(list):
    length=len(list)
    for index in range(length):
        for i in range(index,length):
            #print(index, i)
            if list[index]<list[i]:
                list[index],list[i]=list[i],list[index]

    return list

#test
list=[10,23,1,53,654,54,16,646,65,3155,546,31]
print (select_sort(list))