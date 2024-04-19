def search_sq(N, W, H):
    min_side = 1
    max_side = max(W, H) * N
    while min_side < max_side:
        mid = min_side + (max_side - min_side) // 2
        if verify_capacity(W, H, N, mid):
            max_side = mid
        else:
            min_side = mid + 1
    return max_side


def verify_capacity(w, h, n, x):
    value = (x // w) * (x // h)
    if value >= n:
        return True
    else:
        return False
