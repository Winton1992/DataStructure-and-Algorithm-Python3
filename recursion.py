def ca(n):
    if n == 1:
        return 1
    return n*ca(n-1)

print(ca(5))

#process of recursion

#(ca(5))

#(4 * ca(5))

#(3 * (4 * ca(5)))

#(2 * (3 * (4 * ca(5))))

#(1 * (2 * (3 * (4 * (5)))))

