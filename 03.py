from collections import defaultdict

with open('03.txt') as f:
    lines = f.readlines()

x = defaultdict(int)


#1 @ 1,3: 4x4
overlaps = []

class Node:
    def __init__(self, pos, size, id_):
      self.pos = pos
      self.size = size
      self.id = id_

    def __str__(self):
      return self.id

for line in lines:
    id_, _, pos, size = line.split(' ')
    pos = tuple(map(int, pos.replace(':', '').split(',')))
    size = tuple(map(int, size.split('x')))
    n = Node(pos, size, id_)
    no_overlap = True
    to_remove = set()
    for i in range(size[0]):
        for j in range(size[1]):
            if x[(pos[0]+i, pos[1]+j)] > 0:
                no_overlap = False
                for nn in overlaps:
                    overlap_pos, overlap_size = nn.pos, nn.size
                    if overlap_pos[0] <= pos[0]+i <= overlap_pos[0] + overlap_size[0] and overlap_pos[1] <= pos[1]+j <= overlap_pos[1] + overlap_size[1]:
                        to_remove.add(nn)
                        break
            x[(pos[0]+i, pos[1]+j)] += 1
    for to_rem in to_remove:
        try:
          overlaps.remove(to_rem)
        except:
          pass
    if no_overlap:
        overlaps.append(n)


sum = 0
for i in range(1000):
    for j in range(1000):
        if x[(i,j)] > 1:
            sum += 1

print(sum)

for o in overlaps:
    print(o)
