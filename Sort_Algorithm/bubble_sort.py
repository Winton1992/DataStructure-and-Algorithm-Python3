#比较相邻的元素。如果第一个比第二个大，就交换他们两个。
#对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
#针对所有的元素重复以上的步骤，除了最后一个。
#持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
def bubble_sort(list):
    length=len(list)
    for index in range(length):  # if length is 5, then index will be 0 1 2 3 4
        for i in range(1,length-index):
            if list[i-1]<list[i]:
                list[i],list[i-1]=list[i-1],list[i] # change position
    return list

list=[10,23,1,53,654,54,16,646,65,3155,546,31]
print (bubble_sort(list))