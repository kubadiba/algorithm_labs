def bfs(hierarchy):
    max_experience = 0
    queue = [(0, 0, 0)]
    front = 0

    while front < len(queue):
        level, position, experience = queue[front]
        front += 1
        if level == len(hierarchy) - 1:
            max_experience = max(max_experience, experience + hierarchy[level][position])
        else:
            queue.append((level + 1, position, experience + hierarchy[level][position]))
            queue.append(
                (level + 1, position + 1, experience + hierarchy[level][position])
            )
    return max_experience



with open("source/career.in", "r") as f:
    L = int(f.readline())
    hierarchy = []
    for _ in range(L):
        hierarchy.append(list(map(int, f.readline().split())))

max_exp = bfs(hierarchy)
with open("source/career.out", "w") as f:
    f.write(str(max_exp))
