def insert(intervals, newInterval):
    res = []
    n = newInterval

    for index, i in enumerate(intervals):
        if i[-1] < n[0]:
            res.append(i)

        elif n[-1] < i[0]:
            res.append(n)
            return res + intervals[index:]

        else:
            n[0] = min(n[0], i[0])
            n[-1] = max(n[-1], i[-1])

    res.append(n)
    return res

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
