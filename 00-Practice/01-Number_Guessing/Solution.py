# import sys

# def eprint(*args, **kwargs):
#     print(*args, file=sys.stderr, **kwargs)

def do_test_case():
    a, b = [int(s) for s in input().split(' ')]
    n = int(input())

    while True:

        # eprint(flush=True)
        # eprint('a: {}'.format(a), flush=True)
        # eprint('b: {}'.format(b), flush=True)
        # eprint('# of tries left: {}'.format(n), flush=True)

        k = (a + b + 1) // 2
        if k <= a:
            k += 1
            if k > b:
                raise ValueError('No candidate left!')
        elif k > b:
            k -= 1
            if k <= a:
                raise ValueError('No candidate left!')

        # n -= 1
        print(k, flush=True)

        # Analyze feedback
        f = input()
        if f == "CORRECT":
            return True
        elif f == "WRONG_ANSWER":
            return False
        elif f == "TOO_BIG":
            b = k - 1
        elif f == "TOO_SMALL":
            a = k
        else:
            raise ValueError(f + '. Feedback not expected!')

# Get number of test cases
t = int(input())

while t > 0:
    r = do_test_case()
    assert r
    t -= 1
