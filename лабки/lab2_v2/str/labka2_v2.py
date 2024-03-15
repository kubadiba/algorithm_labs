def max_value(K, T, L):
    M = len(L)
    time = [0] * M

    for i in range(M):
        time[i] = L[i] * T

    dp = [[0 for _ in range(2)] for _ in range(M)]

    dp[0][0] = 0
    dp[0][1] = time[0]

    for i in range(1, M):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])

        dp[i][1] = time[i]

        if (i - K >= 0):
            dp[i][1] += max(dp[i - K][0], dp[i - K][1])

    return max(dp[M - 1][0], dp[M - 1][1])


K = 2
T = 5
L = [10, 15, 10, 5, 10, 15, 20, 20, 15]

result = max_value(K, T, L)
print("Результат:", result)


