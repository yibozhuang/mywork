import collections

def ladderLength(beginWord, endWord, wordList):
    chars = 'abcdefghijklmnopqrstuvwxyz'

    wordList = set(wordList)
    queue = collections.deque([[beginWord, 1]])

    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length

        for i in range(len(word)):
            for c in chars:
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append([next_word, length + 1])

    return 0

print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
