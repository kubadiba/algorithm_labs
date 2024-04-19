def dfs(level, position, experience, hierarchy):
    if level == len(hierarchy) - 1:
        return hierarchy[level][position]

    left_child = dfs(level + 1, position, experience, hierarchy)
    right_child = dfs(level + 1, position + 1, experience, hierarchy)

    if left_child > right_child:
        return hierarchy[level][position] + left_child
    else:
        return hierarchy[level][position] + right_child


def max_experience(hierarchy):
    return dfs(0, 0, 0, hierarchy)


with open("career.in", "r") as f:
    L = int(f.readline())
    hierarchy = []
    for _ in range(L):
        hierarchy.append(list(map(int, f.readline().split())))

max_exp = max_experience(hierarchy)
with open("career.out", "w") as f:
    f.write(str(max_exp))
