import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()
    left = [int(x.split()[0]) for x in data]
    right = [int(x.split()[1]) for x in data]

    left.sort()
    right.sort()

    total = 0

    for x in left:
        total += x * right.count(x)

    print(total)
