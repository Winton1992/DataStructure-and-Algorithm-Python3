#二分查找,给出一个已经排好序的列表,注意是已经排好序的,查找指定元素在列表中的位置
def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = int((low+high)/2)
        guess = list[mid]
        if guess>item:
            high = mid-1
        elif guess<item:
            low = mid+1
        else:
            return mid
    return None
mylist = [1,3,5,7,9]
print (binary_search(mylist,3))