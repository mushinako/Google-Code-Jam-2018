from math import ceil

t = int(input())

for i in range(1, t+1):
    n, k = [int(r) for r in input().split(' ')]

    # Mark numbers with frequency
    n = [[n, 1]]

    round = 0
    assigned = 1

    while k > assigned:
        # Reverse sort so that the larger blands are at the front
        n.sort(reverse=True)
        # m is the array of blank sizes
        m = [x[0] for x in n]

        # Combine frequencies of same blank sizes
        j = len(m) - 1
        while j > 0:
            if m[j] == m[j-1]:
                n[j-1][1] += n[j][1]
                n[j] = 0
            j -= 1

        # Reestablish number-frequency array, after the people of this round
        # occupy their rooms
        l = [y for y in n if y != 0]
        n = []
        for z in l:
            n.append([ceil((z[0]-1)/2), z[1]])
            n.append([(z[0]-1)//2, z[1]])

        k -= assigned
        round += 1
        assigned *= 2

    # When the number of people left is not sufficient to fill a round
    n.sort(reverse=True)
    f = 0
    while k > n[f][1]:
        # Just assign people from the largest blank
        k -= n[f][1]
        f += 1

    # The answer shows when we run out of people
    print('Case #{}: {} {}'.format(i, ceil((n[f][0]-1)/2), (n[f][0]-1)//2))
