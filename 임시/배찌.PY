# 2a + b + 3c = curry
# a, b, c = 20, 9, 22

a, b, c = 20, 9, 22
count = 0

while a >= 2 and b >= 1 and c >= 3:
    a -= 2
    b -= 1
    c -= 3
    print(a, b, c)
    count += 1


print(count)