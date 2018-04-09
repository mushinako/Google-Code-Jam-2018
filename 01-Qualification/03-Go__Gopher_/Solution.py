import math

def int_input():
    x = input()
    if x == '-1 -1':
        assert False, 'Somehow the case is false'
    elif x == '0 0':
        return False
    else:
        return [int(i) for i in x.split(' ')]

def fprint(*args, **kwargs):
    print(*args, flush=True, **kwargs)

def do_test_case():
    a = int(input())

    dm = math.ceil(math.sqrt(a))
    # Set initial at 2,2
    fprint('2 2')
    a, b = int_input()
    trees = [[a,b]]
    final_a = a + dm - 1
    final_b = b + dm - 1

    # Starting from initial, hole every block except the last 2 rows & columns
    for j in range(a, final_a-1):
        for k in range(b, final_b-1):
            while not [j, k] in trees:
                fprint('{} {}'.format(j+1, k+1))
                r = int_input()
                if r:
                    if r not in trees:
                        trees.append(r)
                else:
                    return 0

    # Fill the last 2 rows, except the last 2 columns, by repeatedly holing the
    # second-to-last row
    for l in range(a, final_a-1):
        while not (([l, final_b-1] in trees) and ([l, final_b] in trees)):
            fprint('{} {}'.format(l+1, final_b-1))
            r = int_input()
            if r:
                if r not in trees:
                    trees.append(r)
            else:
                return 0

    # Fill the last 2 columns, except the last 2 rows, by repeatedly holing the
    # second-to-last column
    for m in range(b, final_b-1):
        while not (([final_a-1, m] in trees) and ([final_a, m] in trees)):
            fprint('{} {}'.format(final_a-1, m+1))
            r = int_input()
            if r:
                if r not in trees:
                    trees.append(r)
            else:
                return 0

    # Fill the bottom-right two-by-two by repeatedly holing [n-2][n-2]
    while not (([final_a-1, final_b-1] in trees)
               and ([final_a-1, final_b] in trees)
               and ([final_a, final_b-1] in trees)
               and ([final_a, final_b] in trees)):
        fprint('{} {}'.format(final_a-1, final_b-1))
        r = int_input()
        if r:
            if r not in trees:
                trees.append(r)
        else:
            return 0

t = int(input())

while t > 0:
    do_test_case()
    t -= 1
