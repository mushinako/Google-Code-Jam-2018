from math import ceil

class Cashier:
    def __init__(self, m, s, p):
        self.m = m
        self.s = s
        self.p = p

    def pat(self, t):
        return min(self.m, max(0, (t-self.p) // self.s))

# Check if at time *t* the condition is satisfied
def valid_time(t, r, b, cs):
    processed_at_t = [i.pat(t) for i in cs]
    processed_at_t.sort(reverse=True)
    del processed_at_t[r:]
    total = sum(processed_at_t)
    return b <= total

def bit_party(r, b, cs):
    # The time, as an integer, cannot be less than 1
    t = [1, 2]
    while True:
        if not valid_time(t[1], r, b, cs):
            # If the upper bound is not large enough, double it
            t[1] *= 2
        elif valid_time(t[0], r, b, cs):
            # If the lower bound is not small enough, halve it
            t[0] = ceil(t[0] / 2)
        elif t[1] - t[0] == 1:
            # If the lower bound is small and upper bound is large and their
            # difference is 1, then it can be concluded that the upper bound
            # is the smallest satisfactory time
            return t[1]
        else:
            # Binary search
            new_t = sum(t) // 2
            if valid_time(new_t, r, b, cs):
                t[1] = new_t
            else:
                t[0] = new_t

def main():
    t = int(input())
    for i in range(1, t+1):
        r, b, c = [int(j) for j in input().split(' ')]
        cashiers = []
        for k in range(c):
            cashiers.append(Cashier(*[int(j) for j in input().split(' ')]))
        s = bit_party(r, b, cashiers)
        print('Case #{}: {}'.format(i, s))

if __name__ == '__main__':
    main()
