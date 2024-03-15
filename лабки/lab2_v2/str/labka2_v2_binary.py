def can_paint_all(advertisements, painters, time_per_meter, total_time):
    total_meters = 0
    for ad in advertisements:
        total_meters += ad

    return total_meters <= painters * total_time // time_per_meter


def min_time_paint(advertisements, painters, time_per_meter):
    max_length = max(advertisements)
    low = max_length // painters
    high = max_length

    while low < high:
        mid = (low + high) // 2
        if can_paint_all(advertisements, painters, time_per_meter, mid):
            high = mid
        else:
            low = mid + 1
    return low


K = 3
T = 10
L = [5, 7, 3, 8, 4]

min_time = min_time_paint(L, K, T)

if can_paint_all(L, K, T, min_time):
    print("It is possible to paint all shields in the allotted time")
    print("Minimum possible time:", min_time)
else:
    print("Not enough time to paint all the shields")
