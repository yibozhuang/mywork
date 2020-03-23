from typing import List

def shortestToChar(S: str, C: str) -> List[int]:
    n = len(S)
    res = [n] * n
    pos = -n

    for i in list(range(n)) + list(range(n)[::-1]):
        if S[i] == C:
            pos = i

        res[i] = min(res[i], abs(i - pos))

    return res

print(shortestToChar('loveleetcode', 'e'))
