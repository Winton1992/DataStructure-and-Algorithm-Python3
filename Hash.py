def hash(string, tablesize):
    sum = 0
    for pos in range(len(string)):
        sum = sum + ord(string[pos])

    return sum%tablesize


str = ["a"]
print(hash(str, 11))

