def saving_the_universe_again(d, p):
    # Assuming all shoots damage 1, the shield can't stand it if
    # the number of shoots is greater than the shield strength
    if p.count('S') > d:
        print('Case #{}: IMPOSSIBLE'.format(i))
    else:
        s_index = []
        for j in range(len(p)):
            if p[j] == 'S':
                s_index.append(j)

        # If there are no shoots, no need to swap then
        if len(s_index) == 0:
            print('Case #{}: 0'.format(i))
        else:
            s_damage = [2**s_index[0]]
            for k in range(1, len(s_index)):
                # The number of charges between next and previous damage is
                # (the index difference - 1)
                s_damage.append(s_damage[-1]*2**(s_index[k]-s_index[k-1]-1))

            swap = 0
            while d < sum(s_damage):
                # Halve the last one as it does most damage by swapping the
                # first 'C' before it with the immediately following 'S'
                s_damage[-1] //= 2
                s_damage.sort()
                swap += 1
            return swap

def main():
    t = int(input())

    for i in range(1, t+1):
        n, s = input().split(' ')
        r = saving_the_universe_again(int(n), list(s))
        print('Case #{}: {}'.format(i, swap))

if __name__ == '__main__':
    main()
