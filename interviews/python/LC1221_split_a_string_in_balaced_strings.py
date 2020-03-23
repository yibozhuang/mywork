def balancedStringSplit(s: str) -> int:
    res = 0
    cnt = 0

    for c in s:
        cnt += (c == 'L')
        cnt -= (c == 'R')
        res += (cnt == 0)

    return res


print(balancedStringSplit("RLRRRLLRLL"))
