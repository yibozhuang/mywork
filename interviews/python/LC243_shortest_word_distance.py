def shortestDistance(words, word1, word2):
    result = []
    for i, w in enumerate(words):
        if w == word1:
            if word2 in words[i:]:
                result.append(abs(words[i:].index(word2)))

        if w == word2:
            if word1 in words[i:]:
                result.append(abs(words[i:].index(word1)))

    return min(result)

print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))
