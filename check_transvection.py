"""Small exact check of the pure braid word in candidate Lemma 4.1.

Arithmetic is in Z[z]/(z^2+z+1). No data or finite group is enumerated.
This verifies a displayed identity; it is not an independent proof audit.
"""

ZERO = (0, 0)
ONE = (1, 0)
Z = (0, 1)
ZBAR = (-1, -1)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[0], -x[1]


def multiply(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def conjugate(x):
    return x[0] - x[1], -x[1]


def matrix(rows):
    return [[(x, 0) if isinstance(x, int) else x for x in row] for row in rows]


IDENTITY = matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
ZERO_MATRIX = matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])


def matmul(a, b):
    result = []
    for i in range(3):
        row = []
        for j in range(3):
            entry = ZERO
            for k in range(3):
                entry = add(entry, multiply(a[i][k], b[k][j]))
            row.append(entry)
        result.append(row)
    return result


def product(*matrices):
    result = IDENTITY
    for item in matrices:
        result = matmul(result, item)
    return result


def power(a, exponent):
    result = IDENTITY
    for _ in range(exponent):
        result = matmul(result, a)
    return result


def subtract(a, b):
    return [[add(a[i][j], neg(b[i][j])) for j in range(3)] for i in range(3)]


r1 = matrix([[neg(Z), 1, 0], [0, 1, 0], [0, 0, 1]])
r2 = matrix([[1, 0, 0], [Z, neg(Z), 1], [0, 0, 1]])
r3 = matrix([[1, 0, 0], [0, 1, 0], [0, Z, neg(Z)]])
gram = matrix([[1, ZBAR, 0], [Z, 1, ZBAR], [0, Z, 1]])

for reflection in (r1, r2, r3):
    assert power(reflection, 6) == IDENTITY
    transpose = list(map(list, zip(*reflection)))
    barred = [[conjugate(x) for x in row] for row in reflection]
    assert product(transpose, gram, barred) == gram

# The inverse of a reflection is its fifth power; reverse words for u^-1.
r1_inverse, r2_inverse = power(r1, 5), power(r2, 5)
u = product(r1, r2_inverse)
u_inverse = product(r2, r1_inverse)
v = product(r1, u, r1_inverse)
v_inverse = product(r1, u_inverse, r1_inverse)
commutator = product(u, v, u_inverse, v_inverse)
nilpotent = subtract(commutator, IDENTITY)
expected = matrix([[0, 0, (-1, 1)], [0, 0, (-2, -1)], [0, 0, 0]])
assert nilpotent == expected
assert matmul(nilpotent, nilpotent) == ZERO_MATRIX
assert multiply((2, 1), conjugate((2, 1))) == (3, 0)
assert product(r1, r2, r1) == product(r2, r1, r2)
assert product(r2, r3, r2) == product(r3, r2, r3)
print("Exact identity verified; coefficient norm 3; square-zero rank-one direction.")
