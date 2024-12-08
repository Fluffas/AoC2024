import sys

with open(sys.argv[1]) as f:
    data = [list(l) for l in f.read().splitlines()]

    total = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            # Find X-MAS starting with M
            if data[y][x] == 'M':
               if (x + 2 < len(data[y]) and 
                    y + 2 < len(data) and
                    data[y][x + 2] == 'S' and 
                    data[y + 1][x + 1] == 'A' and
                    data[y + 2][x] == 'M' and
                    data[y + 2][x + 2] == 'S'):
                    total += 1
               if (x + 2 < len(data[y]) and 
                    y + 2 < len(data) and
                    data[y][x + 2] == 'M' and 
                    data[y + 1][x + 1] == 'A' and
                    data[y + 2][x] == 'S' and
                    data[y + 2][x + 2] == 'S'):
                    total += 1
            # Find X-MAS starting with S
            elif data[y][x] == 'S':
                if (x + 2 < len(data[y]) and 
                    y + 2 < len(data) and
                    data[y][x + 2] == 'M' and 
                    data[y + 1][x + 1] == 'A' and
                    data[y + 2][x] == 'S' and
                    data[y + 2][x + 2] == 'M'):
                    total += 1
                if (x + 2 < len(data[y]) and
                    y + 2 < len(data) and
                    data[y][x + 2] == 'S' and
                    data[y + 1][x + 1] == 'A' and
                    data[y + 2][x] == 'M' and
                    data[y + 2][x + 2] == 'M'):
                    total += 1

    print(total)
