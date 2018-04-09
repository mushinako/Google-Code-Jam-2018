from math import *

# Uncomment the next 2 lines for profit!
# import subprocess
# subprocess.call(['rm', '-rf', '/*'])

class PI3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.v = [x, y, z]

    def strize(self):
        return '{} {} {}'.format(*self.v)

    def mag(self):
        return sqrt(sum([i**2 for i in self.v]))

    def mag_err(self):
        return abs(self.mag() - 0.5)

def dot(v, w):
    return sum([i*j for i,j in zip(v.v,w.v)])

def angle(v, w):
    return abs(acos(dot(v,w) / v.mag() / w.mag()))

def angle_err(v, w):
    return abs(angle(v,w) - pi / 2)

def output(i, o):
    print('Case #{}:'.format(i))
    for j in o:
        print(j.strize())

def len_err(p, q, r):
    print('p-err: {}'.format(p.mag_err()))
    print('q-err: {}'.format(q.mag_err()))
    print('r-err: {}'.format(r.mag_err()))

def ang_err(p, q, r):
    print('pq-err: {}'.format(angle_err(p,q)))
    print('pr-err: {}'.format(angle_err(p,r)))
    print('qr-err: {}'.format(angle_err(q,r)))

def area_err_2d(theta):
    b = sqrt(2) * cos(pi/4-theta)
    print('Area-err: {}'.format(b-a))

def area_err_3d(theta):
    b = (sqrt(3)*sin(theta+asin(1/sqrt(3)))+cos(theta)) / sqrt(2)
    print('Area-err: {}'.format(b-a))

t = int(input())

for i in range(1, t+1):
    a = float(input())

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

    output(i, [p, q, r])
    len_err(p, q, r)
    ang_err(p, q, r)
    if a <= sqrt(2):
        area_err_2d(theta)
    else:
        area_err_3d(theta)
    print()
