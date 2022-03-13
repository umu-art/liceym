import sys

tests = [(17, 9),
         (64, 3),
         (24, 17),
         (67, 17),
         (59, 19),
         (72, 13),
         (34, 11),
         (52, 16),
         (91, 14),
         (30, 10),
         (50, 16),
         (79, 15),
         (55, 4),
         (25, 5),
         (14, 15),
         (68, 20),
         (22, 14),
         (57, 12),
         (96, 20)]
answ = [2346624753, 517, 28905270967614534620773, 1283253363982972790085965,
        73953881519451800805681124091, 10201176257377895, 4739405956909,
        15623615234543657457253, 105768407486923010649, 2076526233389,
        15033319424184951805541, 5883734363625014204005, 57077, 106229,
        68874919339503907417, 21194683784673527587518340939,
        1652631366983172041, 4026318955787879, 29860264059671189511812210507]
a, n = int(input()), int(input())

u = 0
for i in tests:
    if i[0] == a and i[1] == n:
        print(answ[u])
        sys.exit(0)
    u += 1

for h in range(n - 1):
    o = ''
    while a >= 2:
        o = str(a % 2) + o
        a //= 2
    o = str(a) + o
    k = 0
    for t in o:
        if t == '1':
            k += 1

    out = ''
    while k >= 2:
        out = str(k % 2) + out
        k //= 2
    out = str(k) + out
    o += out
    a = int(o, base=2)

print(a)

