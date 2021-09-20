n = int(input())

word1 = []
word3 = []

for i in range(n):
    w = input()
    word1.append(w)
    word2 = list(map(str, w))

for i in range(n):
    for j in range(n):
        print(word2[j][i])
        word3.append(word2[j][i])

print(word2)
print(word3)