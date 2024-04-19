def monoton(array):
    increasing = decreasing = True

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            decreasing = False
        elif array[i] < array[i - 1]:
            increasing = False

    return increasing or decreasing


print(monoton([2, 2, 2, 2, 2]))
print(monoton([2, 2, 2, 2, 3]))
print(monoton([2, 2, 2, 2, 1]))
