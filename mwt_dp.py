import numpy as np

def mwt_dp(P):
    n = len(P)
    if n <= 3:
        return 0

    dp = np.full((n, n), float('inf'))
    for i in range(n):
        dp[i][(i+1)%n] = 0

    def dist(i, j):
        return np.linalg.norm(np.array(P[i]) - np.array(P[j]))

    for length in range(2, n):
        for i in range(n):
            j = (i + length) % n
            for k in range(1, length):
                k_abs = (i + k) % n
                cost = dp[i][k_abs] + dp[k_abs][j] + dist(i, j)
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n-1]  # Minimum weight for full polygon
