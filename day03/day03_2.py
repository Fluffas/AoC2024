import sys
import re

with open(sys.argv[1]) as f:
    data = f.read()
    regex = r"(do|don't)\(\)|mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(regex, data)

    total = 0
    do = True
    for d, x, y in matches:
        if d == "do":
            do = True
        elif d == "don't":
            do = False
        else:
            if do:
                total += int(x) * int(y)

    print(total)