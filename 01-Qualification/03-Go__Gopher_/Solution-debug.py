import sys
from math import ceil, sqrt

def int_input():
    x = input()
    if x == '-1 -1':
        assert False, 'Somehow the case is false'
    elif x == '0 0':
        return False
    else:
        return [int(i) for i in x.split(' ')]

def eprint(*args, **kwargs):
    fprint(*args, file=sys.stderr, **kwargs)

def fprint(*args, **kwargs):
    print(*args, flush=True, **kwargs)

def go__gopher_():
    a = int(input())

    ## As A is either 20 or 200, we can set wanted dimensions
    # if a == 20:
    #     dm = [4, 5]
    # elif a == 200:
    #     dm = [10, 20]
    # else:
    #     raise ValueError('Testing case not 20 or 200!')

    dm = ceil(sqrt(a))
    # Set initial at 2,2
    fprint('2 2')
    a, b = int_input()
    trees = [[a,b]]
    final_a = a + dm - 1
    final_b = b + dm - 1

    eprint('Dimension: {}'.format(dm))
    eprint('Starting: {}'.format([a,b]))
    eprint()

    for j in range(a, final_a-1):
        for k in range(b, final_b-1):
            eprint('Now on: {}'.format([j,k]))
            while not [j, k] in trees:
                eprint('{} not holed'.format([j,k]))
                fprint('{} {}'.format(j+1, k+1))
                r = int_input()
                if r:
                    if r not in trees:
                        trees.append(r)
                        eprint('{} newly holed'.format(r))
                    else:
                        eprint('{} already holed'.format(r))
                else:
                    return 0
                eprint()

    for l in range(a, final_a-1):
        eprint('Now on: {} and {}'.format([l,final_b-1], [l,final_b]))
        while not (([l, final_b-1] in trees) and ([l, final_b] in trees)):
            eprint('{} and/or {} not holed'.format([l,final_b-1], [l,final_b]))
            fprint('{} {}'.format(l+1, final_b-1))
            r = int_input()
            if r:
                if r not in trees:
                    trees.append(r)
                    eprint('{} newly holed'.format(r))
                else:
                    eprint('{} already holed'.format(r))
            else:
                return 0
            eprint()

    for m in range(b, final_b-1):
        eprint('Now on: {} and {}'.format([final_a-1,m], [final_a,m]))
        while not (([final_a-1, m] in trees) and ([final_a, m] in trees)):
            eprint('{} and/or {} not holed'.format([final_a-1,m], [final_a,m]))
            fprint('{} {}'.format(final_a-1, m+1))
            r = int_input()
            if r:
                if r not in trees:
                    trees.append(r)
                    eprint('{} newly holed'.format(r))
                else:
                    eprint('{} already holed'.format(r))
            else:
                return 0
            eprint()

    eprint('Now on: {} and {} and {} and {}'.format([final_a-1,final_b-1],
                                                    [final_a-1,final_b],
                                                    [final_a,final_b-1],
                                                    [final_a,final_b]))
    while not (([final_a-1, final_b-1] in trees)
               and ([final_a-1, final_b] in trees)
               and ([final_a, final_b-1] in trees)
               and ([final_a, final_b] in trees)):
        eprint('{} and/or {} and/or {} and/or {} not holed'.format(
            [final_a-1,final_b-1],
            [final_a-1,final_b],
            [final_a,final_b-1],
            [final_a,final_b]))
        fprint('{} {}'.format(final_a-1, final_b-1))
        r = int_input()
        if r:
            if r not in trees:
                trees.append(r)
                eprint('{} newly holed'.format(r))
            else:
                eprint('{} already holed'.format(r))
        else:
            return 0
        eprint()

def main():
    t = int(input())

    while t > 0:
        go__gopher_()
        eprint('\n')
        t -= 1

if __name__ == '__main__':
    main()
