n, s = input().split()
names = []
players = []
count = 0
answer = ""

for i in range(int(n)):
    name, player = map(str, input().split())
    names.append(name)
    players.append(player)
    
ans = list(zip(names, players))

for i in ans:
    if i[0] == s:
        answer += i[1]

for i in ans:
    if i[0] != s and i[1] == answer:
        count += 1
    if i[0] == s and i[1] == answer:
        break

print(count)