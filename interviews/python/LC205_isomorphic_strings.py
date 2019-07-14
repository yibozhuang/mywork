def isIsomorphic(s, t):
    d1 = {}
    d2 = {}

    for i, val in enumerate(s):
        if val in d1:
            d1[val].append(i)
        else:
            d1[val] = [i]

    for i, val in enumerate(s):
        if val in d2:
            d2[val].append(i)
        else:
            d2[val] = [i]

    return sorted(d1.values()) == sorted(d2.values())

print(isIsomorphic("paper", "title"))
