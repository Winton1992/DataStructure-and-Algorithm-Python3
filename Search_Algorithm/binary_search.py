#二分查找,给出一个已经排好序的列表,注意是已经排好序的,查找指定元素在列表中的位置
def binarySearch(list, item):
    first = 0
    last = len(list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))