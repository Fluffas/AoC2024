import sys

def check_valid(x):
    if all(x[i] - x[i + 1] >= 1 and x[i] - x[i + 1] <= 3 for i in range(len(x) - 1)):
        return True
    elif all(x[i + 1] - x[i] >= 1 and x[i + 1] - x[i] <= 3 for i in range(len(x) - 1)):
        return True
    else:
        return False

with open(sys.argv[1]) as f:
    data = [[int(x) for x in l.split()] for l in f.read().splitlines()]

    total = 0
    not_guaranteed_safe = []
    for x in data:
        if check_valid(x):
            total += 1
        else:
            not_guaranteed_safe.append(x)

    for x in not_guaranteed_safe:
        # Find the first mistake in the list
        # Remove the element where the mistake occurs
        # Also try removing the next element as this could be the mistake
        # Check if either of these resulting lists are valid

        # Determine if a list is increasing or decreasing
        increasing = False
        increase_count = 0
        decrease_count = 0
        for i in range(len(x) - 1):
            if x[i] - x[i + 1] > 0:
                decrease_count += 1
            elif x[i + 1] - x[i] > 0:
                increase_count += 1

        if increase_count > decrease_count:
            increasing = True

        if increasing:
            first = True
            for i in range(len(x) - 1):

                if x[i + 1] - x[i] >= 1 and x[i + 1] - x[i] <= 3:
                    first = False
                    continue

                # Remove current element and check if it is valid
                current_removed = x.copy()
                current_removed.pop(i)
                if check_valid(current_removed):
                    total += 1
                    break

                # Remove next element and check if it is valid
                next_removed = x.copy()
                next_removed.pop(i + 1)
                if check_valid(next_removed):
                    total += 1
                    break

                # Not valid
                break
                
        else:
            first = True
            for i in range(len(x) - 1):

                if x[i] - x[i + 1] >= 1 and x[i] - x[i + 1] <= 3:
                    first = False
                    continue

                # Remove current element and check if it is valid
                current_removed = x.copy()
                current_removed.pop(i)
                if check_valid(current_removed):
                    total += 1
                    break

                # Remove next element and check if it is valid
                next_removed = x.copy()
                next_removed.pop(i + 1)
                if check_valid(next_removed):
                    total += 1
                    break

                # Not valid
                break
                
    print(total)