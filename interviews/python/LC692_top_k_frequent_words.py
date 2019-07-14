def topKFrequent(words, k):
    dic = {}
    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    ret = sorted(dic, key=dic.get, reverse=True)

    return ret[:k]

print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
