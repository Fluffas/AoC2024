import sys

with open(sys.argv[1]) as f:
    data = [list(l) for l in f.read().splitlines()]

    total = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'X':
                # Check right
                if x + 3 < len(data[y]) and data[y][x + 1] == 'M' and data[y][x + 2] == 'A' and data[y][x + 3] == 'S':
                    total += 1

                # Check left
                if x - 3 >= 0 and data[y][x - 1] == 'M' and data[y][x - 2] == 'A' and data[y][x - 3] == 'S':
                    total += 1

                # Check up
                if y - 3 >= 0 and data[y - 1][x] == 'M' and data[y - 2][x] == 'A' and data[y - 3][x] == 'S':
                    total += 1

                # Check down
                if y + 3 < len(data) and data[y + 1][x] == 'M' and data[y + 2][x] == 'A' and data[y + 3][x] == 'S':
                    total += 1

                # Check diagonal up-right
                if x + 3 < len(data[y]) and y - 3 >= 0 and data[y - 1][x + 1] == 'M' and data[y - 2][x + 2] == 'A' and data[y - 3][x + 3] == 'S':
                    total += 1

                # Check diagonal up-left
                if x - 3 >= 0 and y - 3 >= 0 and data[y - 1][x - 1] == 'M' and data[y - 2][x - 2] == 'A' and data[y - 3][x - 3] == 'S':
                    total += 1

                # Check diagonal down-right
                if x + 3 < len(data[y]) and y + 3 < len(data) and data[y + 1][x + 1] == 'M' and data[y + 2][x + 2] == 'A' and data[y + 3][x + 3] == 'S':
                    total += 1

                # Check diagonal down-left
                if x - 3 >= 0 and y + 3 < len(data) and data[y + 1][x - 1] == 'M' and data[y + 2][x - 2] == 'A' and data[y + 3][x - 3] == 'S':
                    total += 1

    print(total)
