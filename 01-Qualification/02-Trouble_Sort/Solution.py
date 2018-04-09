t = int(input())

for i in range(1, t+1):
    n = input()
    v = [int(j) for j in input().split(' ')]

    # Separate the values on even and odd indexes
    v_ieven = []
    v_iodd = []

    for k in range(n):
        if k % 2:
            v_iodd.append(v[k])
        else:
            v_ieven.append(v[k])

    v_ieven.sort()
    v_iodd.sort()

    valid = True

    for l in range(n-1):
        if l % 2:
            if v_iodd[(l-1)//2] > v_ieven[(l+1)//2]:
                valid = False
                error = l
                break
        else:
            if v_ieven[l//2] > v_iodd[l//2]:
                valid = False
                error = l
                break

    if valid:
        print('Case #{}: OK'.format(i))
    else:
        print('Case #{}: {}'.format(i, error))
