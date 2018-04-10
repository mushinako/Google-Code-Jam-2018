from math import *

# Uncomment the next 2 lines for profit!
# import subprocess
# subprocess.call(['rm', '-rf', '/*'])

class PI3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

def output(i, o):
    print('Case #{}:'.format(i))
    for j in o:
        print('{} {} {}'.format(j.x, j.y, j.z))

def cubic_ufo(a):
    # Maximum value sqrt(3)
    if a > sqrt(3) or a < 1:
        raise ValueError('Not possible!')

    # If area less than sqrt(2), then it can be reduced to a 2d problem
    elif a <= sqrt(2):
        theta = asin(a**2 - 1) / 2

        p = PI3D(x=cos(theta)/2, y=sin(theta)/2)
        q = PI3D(x=-p.y, y=p.x)
        r = PI3D(z=0.5)

    # If 3d really has to be dealt with, rotate pi/4 in xy-plane then theta
    # in yz-plane
    else:
        # Solve a = sin(theta) + sqrt(2) * cos(theta)
        theta = 2 * atan((1-sqrt(3-a**2))/(a+sqrt(2)))

        p = PI3D(x=sqrt(2)/4, y=sqrt(2)/4*cos(theta), z=sqrt(2)/4*sin(theta))
        q = PI3D(x=p.x, y=-p.y, z=-p.z)
        r = PI3D(y=-sin(theta)/2, z=cos(theta)/2)

    return [p, q, r]

def main():
    t = int(input())
    for i in range(1, t+1):
        l = cubic_ufo(float(input()))
        output(i, l)

if __name__ == '__main__':
    main()
