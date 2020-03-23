from typing import List

def dailyTemperatures(T: List[int]) -> List[int]:
    n = len(T)
    right_max = float('-inf')

    res = [0] * n

    for i in range(n-1, -1, -1):
        t = T[i]
        if right_max <= t:
            right_max = t
        else:
            temp = 1
            while T[i+temp] <= t:
                temp += res[i+temp]

            res[i] = temp

    return res


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
