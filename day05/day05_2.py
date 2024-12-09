import sys
import networkx as nx


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

    # Find unsafe updates
    unsafe_updates = []
    for update in updates:
        correct = []
        correct.append(update[0])
        for u in update:
            if u in correct:
                if u in rules.keys():
                    # Check if previous u is in rules for current u, if this is the case it is not safe
                    for pu in update[:update.index(u)]:
                        if pu in rules[u]:
                            if update not in unsafe_updates:
                                unsafe_updates.append(update)
                            break

                    correct.extend(rules[u])
            else:
                unsafe_updates.append(update)
                break

    # Fix unsafe updates
    total = 0
    for update in unsafe_updates:
        graph = {}
        for u in update:
            if u in rules.keys():
                r = [up for up in rules[u] if up in update]
                graph[u] = r
        G = nx.DiGraph(graph)

        paths_to_check = []
        for u in update:
            for u2 in update:
                if u == u2:
                    continue

                simple_paths = nx.all_simple_paths(G, source=u, target=u2)
                for path in simple_paths:
                    if len(path) == len(update):
                        paths_to_check.append(path)

        # Check if path is valid
        for update in paths_to_check:
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
