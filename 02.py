from collections import Counter

with open('02.txt') as f:
    lines = f.readlines()

threes, twos = 0, 0
for line in lines:
    counts = Counter(line)
    for char, num in counts.items():
        if num == 2:
            twos += 1
            break

    for char, num in counts.items():
        if num == 3:
            threes += 1
            break
print(twos*threes)


for line in lines:
    for compare in lines:
        if line == compare:
            continue
        first_strike = True
        found = False
        for index in range(len(line)):
            if line[index] == compare[index]:
                continue
            if first_strike:
                first_strike = False
                continue
            break
        else:
            print(f"Found \n{line}{compare}")
            break
