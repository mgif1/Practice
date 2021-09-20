n = int(input())
rs = []
gs = []
bs = []
rgb = []

for i in range(n):
    r, g, b = map(int, input().split())
    rs.append(r)
    gs.append(g)
    bs.append(b)

ri, gi, bi = map(int, input().split())
rgb.append(ri)
rgb.append(gi)
rgb.append(bi)
print(rgb)

mrgb = [int(1/n*sum(rs)), int(1/n*sum(gs)), int(1/n*sum(bs))]
print(mrgb)

ans = list(zip(mrgb, rgb))
answer = list(map(lambda x : abs(x[0]-x[1]), ans))
print(sum(answer))
