#백준 20112번

n = int(input())

word = []
word1 = []
word2 = []

for i in range(n):
    w = input()
    word.append(w)
    for j in w:
        word1.append(j)

for i in range(n):
    for j in range(n):
        word2.append(word[j][i])

if word1 == word2:
    print("YES")
else:
    print("NO")