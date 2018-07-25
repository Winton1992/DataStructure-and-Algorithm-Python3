def shell_sort(list):
    length = int(len(list))
    gap = int(length / 2)
    while gap > 0:
        for i in range(gap, length):
            temp = list[i]
            j = i
            while j >= gap and temp < list[j - gap]:
                list[j] = list[j - gap]
                j = j - gap
            list[j] = temp
        gap = int(gap/2)
    return list


# test
list = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
print(shell_sort(list))
