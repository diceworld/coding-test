n = int(input())

d = [-1] * 91

d[0] = 0
d[1] = 1
d[2] = 1


def f(x):
    if d[x] != -1:
        return d[x]
    d[x] = f(x - 1) + f(x - 2)
    return d[x]


print(f(n))
