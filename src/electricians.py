import math

def calculate_distance_between_poles(w, h1, h2):
    return math.sqrt(w**2 + (h2 - h1) ** 2)

def max_wire_length_required(w, heights):
    num_poles = len(heights)

    max_lengths = [0] * num_poles

    prev_max_heights = [0] * (heights[0] + 1)

    for h in range(1, heights[0] + 1):
        prev_max_heights[h] = 0

    for i in range(1, num_poles):
        current_max_heights = [0] * (heights[i] + 1)
        for h2 in range(1, heights[i] + 1):
            current_max_heights[h2] = max(
                prev_max_heights[h1] + calculate_distance_between_poles(w, h1, h2)
                for h1 in range(1, heights[i - 1] + 1)
            )
        prev_max_heights = current_max_heights

    max_length_required = max(prev_max_heights)

    return max_length_required

test_cases = [
    (2, [3, 3, 3]),
    (100, [1, 1, 1, 1]),
    (4, [100, 2, 100, 2, 100]),
    (
        4,
        [
            56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28, 2, 95, 97, 60, 93,
            40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72,
        ],
    ),
]

for i, (w, heights) in enumerate(test_cases):
    result = max_wire_length_required(w, heights)
    print(f"Тестовий випадок {i + 1}: {result:.2f}")

