rules_map = dict()

with open('input_day5_1.txt', 'r') as file:
    rules = file.read().splitlines()

    for rule in rules:
        split = rule.split('|')
        key = int(split[0])
        value = int(split[1])
        if key not in rules_map:
            rules_map[key] = set()
        
        rules_map[key].add(value)

mid_total = 0
incorrect_orders = list()

with open('input_day5_2.txt', 'r') as file:
    for line in file:
        seen = set()
        values = line.strip().split(',')

        overlapped = False

        for value in values:
            overlap = seen.intersection(rules_map[int(value)])
            if overlap:
                overlapped = True
                break

            seen.add(int(value))

        if not overlapped:
            # Find middle number in the values list
            mid = values[len(values) // 2]
            mid_total += int(mid)
        else:
            incorrect_orders.append([int(s) for s in values]) # Convert to an int list for part 2

print(f"Part 1: {mid_total}")
mid_total = 0

# Part 2
incorrect_orders = [set(order) for order in incorrect_orders] # Convert to sets

for order in incorrect_orders:
    correct_order = list()

    # Loop over each element in the order, check for no overlap
    for value in order:
        overlap = order.intersection(rules_map[value])
        if not overlap:
            correct_order.append(value)

print(f"Part 2: {mid_total}")