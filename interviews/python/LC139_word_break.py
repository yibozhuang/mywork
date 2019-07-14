def wordBreak(s, wordDict):
    ok = [True]
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
    return ok[-1]

print(wordBreak("leetcode", ["leet", "code"]))
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
