sum = 0
list = []
with open('01.txt') as f:
    for line in f.readlines():
        list.append(int(line))
        sum += int(line)
print(sum)


def second():
    seen = set()
    sum = 0
    while True:
        for l in list:
            seen.add(sum)
            sum += l
            if sum in seen:
                print(sum)
                return
                
second()
