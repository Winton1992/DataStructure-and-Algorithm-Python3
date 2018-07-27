#随意选择一个数字作为基准，比基准数字大的在右，比基准数字小的在左。

def quick_sort(list, left, right):
    # 快速排序
    if left >= right:
        return list
    base = list[left]
    low = left
    high = right
    while left < right:
        while left < right and list[right] >= base:
            right -= 1
        list[left] = list[right]
        while left < right and list[left] <= base:
            left += 1
        list[right] = list[left]
    list[right] = base
    quick_sort(list, low, left - 1)
    quick_sort(list, left + 1, high)
    return list

list=[3,2,4,1,59,23,13,1,3]
print (list)
quick_sort(list,0,len(list)-1)
print (list)