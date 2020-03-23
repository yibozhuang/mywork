def reverseWords(s: str) -> str:
    splitted = s.split()
    return ' '.join(reversed(splitted))

data = "the sky is blue"
print(reverseWords(data))
