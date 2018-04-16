def waffle_choppers(w, r, c, h, v):
    # Arrays of chips in each row/column
    r_count = [i.count('@') for i in w]
    c_count = [i.count('@') for i in zip(*w)]

    # Number of total chips must be divisible by the number of people
    total = sum(r_count)
    people = (h+1) * (v+1)
    if total % people:
        return False

    # The chops must divide the waffle into pieces with equal number of chips
    r_acc = 0
    r_chop = [0]
    r_tar = total // (h+1)
    for j in range(r):
        r_acc += r_count[j]
        if r_acc == r_tar:
            r_acc = 0
            r_chop.append(j+1)
        elif r_acc > r_tar:
            return False

    c_acc = 0
    c_chop = [0]
    c_tar = total // (v+1)
    for j in range(c):
        c_acc += c_count[j]
        if c_acc == c_tar:
            c_acc = 0
            c_chop.append(j+1)
        elif c_acc > c_tar:
            return False

    # Verify each piece has the number of chips as it should
    each = total // people
    for m in range(1, len(r_chop)):
        for n in range(1, len(c_chop)):
            if sum([i[c_chop[n-1]:c_chop[n]].count('@')
                    for i in w[r_chop[m-1]:r_chop[m]]]) != each:
                return False

    return True

def main():
    t = int(input())
    for i in range(1, t+1):
        r, c, h, v = [int(j) for j in input().split(' ')]
        w = []
        for _ in range(r):
            w.append(list(input()))
        s = waffle_choppers(w, r, c, h, v)
        print('Case #{}: {}'.format(i, 'POSSIBLE' if s else 'IMPOSSIBLE'))

if __name__ == '__main__':
    main()
