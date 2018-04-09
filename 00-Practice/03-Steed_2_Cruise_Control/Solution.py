t = int(input())

for i in range(1, t+1):
    # Distance & Number of horses
    d, n = [int(s) for s in input().split(' ')]
    horses = []
    for j in range(0, n):
        horses.append([int(r) for r in input().split(' ')])

    # Solve for maximum time, which is incidentally the amount of time required
    # for largest speed without passing anyone
    t = max([((d - a[0]) / a[1]) for a in horses])
    v = d / t

    print('Case #{}: {}'.format(i, v))
