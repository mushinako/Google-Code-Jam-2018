def fprint(*args, **kwargs):
    print(*args, flush=True, **kwargs)

def number_guessing():
    a, b = [int(s) for s in input().split(' ')]
    n = int(input())

    while True:
        k = (a + b + 1) // 2
        if k <= a:
            k += 1
            if k > b:
                raise ValueError('No candidate left!')
        elif k > b:
            k -= 1
            if k <= a:
                raise ValueError('No candidate left!')

        fprint(k)

        # Analyze feedback
        f = input()
        if f == "CORRECT":
            break
        elif f == "WRONG_ANSWER":
            assert False
        elif f == "TOO_BIG":
            b = k - 1
        elif f == "TOO_SMALL":
            a = k
        else:
            raise ValueError(f + '. Feedback not expected!')

def main():
    t = int(input())
    while t > 0:
        number_guessing()
        t -= 1

if __name__ == '__main__':
    main()
