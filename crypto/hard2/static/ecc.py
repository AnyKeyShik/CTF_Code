# -*- coding: utf-8 -*-

INF = "Infinity"


def is_point_on_curve(x, y, a, b, p):
    left = (x ** 3 + a * x + b) % p
    right = (y * y) % p

    return left == right


def point_mul(x, y, d, a, p):
    num_bits = lambda n: n > 0 and num_bits(n >> 1) + str(n & 1) or ''

    binstr = num_bits(d)
    x1 = x
    y1 = y

    for c in binstr[1:]:
        x1, y1 = point_add(x1, y1, x1, y1, a, p)

        if c == "1":
            x1, y1 = point_add(x1, y1, x, y, a, p)

    return x1, y1


def point_add(x1, y1, x2, y2, a, p):
    if x1 == INF:
        return x2, y2

    if x2 == INF:
        return x1, y1

    # Points are descrete, normalize them
    x1 %= p
    y1 %= p
    x2 %= p
    y2 %= p

    # Check for doubeling and inverse
    if x1 == x2:
        if y1 == y2:
            inverse = extended_ea(y1 * 2, p)
            s = ((x1 ** 2) * 3 + a) * inverse
        else:
            return INF, INF
    # Point adding
    else:
        inverse = extended_ea(x2 - x1, p)
        s = (y2 - y1) * inverse

    s %= p
    x3 = (s ** 2 - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p

    return x3, y3


def extended_ea(a, b):
    u = t = 1
    v = s = 0

    while b > 0:
        q = a // b
        a, b = b, a - q * b
        u, s = s, u - q * s
        v, t = t, v - q * t

    return u

