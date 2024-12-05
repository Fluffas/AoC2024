import sys

with open(sys.argv[1]) as f:
    data = [[int(x) for x in l.split()] for l in f.read().splitlines()]

    total = 0
    for x in data:

        if all(x[i] - x[i + 1] >= 1 and x[i] - x[i + 1] <= 3 for i in range(len(x) - 1)):
            total += 1
        elif all(x[i + 1] - x[i] >= 1 and x[i + 1] - x[i] <= 3 for i in range(len(x) - 1)):
            total += 1

    print(total)