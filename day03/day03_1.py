import sys
import re

with open(sys.argv[1]) as f:
    data = f.read()
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    muls = [(int(x), int(y)) for x, y in re.findall(regex, data)]

    total = 0
    for x, y in muls:
        total += x * y

    print(total)