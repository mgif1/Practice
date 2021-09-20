# 백준 20949번
import math

n = int(input())
ppi_rank = []

for i in range(n):
    w, h = map(int, input().split())
    ppi = math.sqrt(w**2 + h**2)/77
    ppi_rank.append(ppi)

ppi_rank.sort(key=lambda x: (-x[0], x[1]))
for i in ppi_rank:
    print(i[1])