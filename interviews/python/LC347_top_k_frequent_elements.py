def topKFrequent(nums, k):
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1

    arr = sorted(dic, key=dic.get, reverse=True)
    return arr[:k]

print(topKFrequent([1,1,1,2,2,3], 2))
