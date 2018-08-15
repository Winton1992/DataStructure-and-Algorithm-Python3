#从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完。
def select_sort(list):
    length=len(list)
    for index in range(length):
        for i in range(index,length):
            #print(index, i)
            if list[index]>list[i]:
                list[index],list[i]=list[i],list[index]

    return list

#test
list=[10,23,1,53,654,54,16,646,65,3155,546,31]
print (select_sort(list))

# def bigSorting(unsorted):
#     length = len(unsorted)
#     mid = 0
#     for i in range(length):
#         for j in range(i, length):
#             if unsorted[i] > unsorted[j]:
#                 mid = unsorted[i]
#                 unsorted[i] = unsorted[j]
#                 unsorted[j] = mid
#     return unsorted
#
# unsorted=[31415926535897932384626433832795,1,3,10,3,5]
# print (bigSorting(unsorted))