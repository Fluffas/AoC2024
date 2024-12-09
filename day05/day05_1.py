import sys


with open(sys.argv[1]) as f:
    data = f.read().split('\n\n')

    rules = {}
    for rule in data[0].split('\n'):
        x, y = rule.split('|')
        x = int(x)
        y = int(y)
        if x in rules.keys():
            rules[x].append(y)
        else:
            rules[x] = [y]

    updates = []
    for update in data[1].strip().split('\n'):
        updates.append([int(x) for x in update.split(',')])

    total = 0
    for update in updates:
        safe = True
        correct = []
        correct.append(update[0])
        for u in update:
            if u in correct:
                if u in rules.keys():
                    # Check if previous u is in rules for current u, if this is the case it is not safe
                    for pu in update[:update.index(u)]:
                        if pu in rules[u]:
                            safe = False
                            break

                    correct.extend(rules[u])
            else:
                safe = False
                break

        if safe:
            total += update[int((len(update) - 1) / 2)]

    print(total)
