from string import ascii_uppercase as uc

def senate_evacuation(party_members):
    plan = []
    while sum(party_members) > 0:
        p0 = party_members.index(max(party_members))
        party_members[p0] -= 1
        p1 = party_members.index(max(party_members))
        party_members[p1] -= 1
        if (max(party_members) * 2) > sum(party_members):
            party_members[p1] += 1
            plan.append(uc[p0])
        else:
            plan.append(uc[p0] + uc[p1])
    return ' '.join(plan)

t = int(input())
for i in range(1, t+1):
    n = int(input())
    l = [int(s) for s in input().split(' ')]
    r = senate_evacuation(l)
    print('Case #{}: {}'.format(i, r))
