def minCost(costs):
    if not costs:
        return 0

    dp = costs[0]
    for i in range(1, len(costs)):
        pre = dp[:]
        for j in range(len(costs[0])):
            dp[j] = costs[i][j] + min(pre[:j] + pre[j+1:])

    return min(dp)

print(minCost([[17,2,17],[16,16,5],[14,3,19]]))
