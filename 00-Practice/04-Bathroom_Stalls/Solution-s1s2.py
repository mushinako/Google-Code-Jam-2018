from math import ceil

def bathroom_stalls(n, k):
    # Mark numbers with frequency
    n = [[n, 1]]

    round = 0
    assigned = 0

    while k > (assigned * 2 + 1):
        # Replace each blank with the blanks formed after the middle is
        # occupied
        p = n[:]
        n = []
        for x in p:
            n.append([ceil((x[0]-1)/2), x[1]])
            n.append([(x[0]-1)//2, x[1]])

        # Reverse sort so that the larger blanks are at the front
        n.sort(reverse=True, key=lambda l: l[0])

        # Combine the frequencies of same blank sizes
        q = [y[0] for y in n]
        for j in range(len(q)-1, 0, -1):
            if q[j] == q[j-1]:
                n[j-1][1] += n[j][1]
                n[j] = 0
        n = [z for z in n if z != 0]

        round += 1
        assigned = 2 ** round - 1

    # When the number of people left is not sufficient to fill a round, assign
    # them from blanks with largest size till they run out
    m = 0
    k -= assigned
    while k > n[m][1]:
        k -= n[m][1]
        m += 1
    return [ceil((n[m][0]-1)/2), (n[m][0]-1)//2]

def main():
    t = int(input())
    for i in range(1, t+1):
        n, k = [int(r) for r in input().split(' ')]
        m = bathroom_stalls(n, k)
        print('Case #{}: {} {}'.format(i, *m))

if __name__ == '__main__':
    main()
