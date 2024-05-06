def max_value(k, t, l):
    workers = len(l)
    time = [0] * workers

    for i in range(workers):
        time[i] = l[i] * t

    dp = [[0 for _ in range(2)] for _ in range(workers)]

    dp[0][0] = 0
    dp[0][1] = time[0]

    for i in range(1, workers):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])

        dp[i][1] = time[i]

        if i - k >= 0:
            dp[i][1] += max(dp[i - k][0], dp[i - k][1])

    return max(dp[workers - 1][0], dp[workers - 1][1])
